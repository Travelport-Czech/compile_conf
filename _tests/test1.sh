#!/usr/bin/env bash
export ao3_port=1234

compileConf='../compile_conf'
compileConfEncrypt='../compile_conf_encrypt'

echo
echo "Test vytvoreni noveho configu:"
rm -f test1.conf
result='Ok'
USER=srbt VERSION=xena "${compileConf}" \
    -k test1.key \
    -K test1.rsa.key.priv \
    -D '#' 'DBPassword: {~???}' 'DBPassword: heheslo' \
    -D '#' 'DBClientCharset: utf8' 'DBClientCharset: 	utf16' \
    -D '#' 'DBRctPassword: {~???}' 'DBRctPassword:	rctHeslo' \
    -D '#' 'DBRctUser: root' 'DBRctUser:	karel' \
    production test1.conf.sample test1.conf
if diff test1.conf.out test1.conf; then
  echo 'Ok'
else
  echo 'Failed'
  result='Failed'
fi
rm -f test1.conf
echo
echo "Test pokusu o prepsani neautomatizovaneho configu:"
cp test1.conf.uncompilable test1.conf
USER=srbt VERSION=xena "${compileConf}" \
    -k test1.key \
    -K test1.rsa.key.priv \
    -D '#' 'DBPassword: {~???}' 'DBPassword: heheslo' \
    -D '#' 'DBRctPassword: {~???}' 'DBRctPassword:	rctheslo' \
    -D '#' 'DBRctUser: root' 'DBRctUser:	karel' \
    production test1.conf.sample test1.conf
if diff test1.conf.uncompilable test1.conf; then
  echo 'Ok'
else
  echo 'Failed'
  result='Failed'
fi
rm -f test1.conf
echo
echo "Test korektniho vygenerovani configu:"
cp test1.conf.in test1.conf
USER=srbt VERSION=xena "${compileConf}" \
    -k test1.key \
    -K test1.rsa.key.priv \
    -d test1.diff \
    -D '#' 'DBRctPassword: {~???}' 'DBRctPassword:	rctheslo' \
    -D '#' 'DBRctUser: root' 'DBRctUser:	karel' \
    production test1.conf.sample test1.conf
# DBRctPassword pretluce definice z test1.conf
# DBRctUser se vezme z definice -D
if diff test1.conf.out test1.conf; then
  echo 'Ok'
else
  echo 'Failed'
  result='Failed'
fi
echo "Kontrola vygenerovaneho diff souboru:"
if diff -I '^\(---\|+++\).*' test1.conf.diff test1.diff; then
  echo 'Ok'
else
  echo 'Failed'
  result='Failed'
fi
rm test1.diff
echo
echo "Test opakovaneho generovani configu bez zmeny:"
USER=srbt VERSION=xena "${compileConf}" \
    -k test1.key \
    -K test1.rsa.key.priv \
    -D '#' 'DBRctPassword: {~???}' 'DBRctPassword:  rctheslo' \
    -D '#' 'DBRctUser: root' 'DBRctUser:  karel' \
    production test1.conf.sample test1.conf
if diff test1.conf.out test1.conf; then
  echo 'Ok'
else
  echo 'Failed'
  result='Failed'
fi
rm -f test1.conf test1.conf.old

echo
echo "Test zasifrovani promenne:"
encrypted=$("${compileConfEncrypt}" --rsa -k test1.rsa.key <<< "hokus")
echo
printf '#compilable conf\nHokus: %s\n' "$encrypted" > test1a.conf.sample
printf '# tento soubor vznikl generovanim pomoci compile_conf z test1a.conf.sample\nHokus: hokus\n' > test1a.conf.out
rm -f test1a.conf
"${compileConf}" \
    -K test1.rsa.key.priv \
    production test1a.conf.sample test1a.conf

if diff test1a.conf.out test1a.conf; then
  echo 'Ok'
else
  echo 'Chyba dekodovani rsa!'
  result='Failed'
fi
rm -f test1a.conf.sample test1a.conf.out test1a.conf

echo
echo "Test zasifrovani dlouhe promenne:"
orig="hokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokushokus"
encrypted=$("${compileConfEncrypt}" --rsa -k test1.rsa.key <<< "$orig" | tr -d '\n')
chunkCount="$(grep -o -F '{~$' <<< "$encrypted" | wc -l)"
echo
if [[ "$chunkCount" == 2 ]]; then
  printf '#compilable conf\nHokus: %s\n' "${encrypted}" > test1a.conf.sample
  printf '# tento soubor vznikl generovanim pomoci compile_conf z test1a.conf.sample\nHokus: %s\n' "$orig" > test1a.conf.out
  rm -f test1a.conf
  "${compileConf}" \
      -K test1.rsa.key.priv \
      production test1a.conf.sample test1a.conf

  if diff test1a.conf.out test1a.conf; then
    echo 'Ok'
  else
    echo 'Chyba dekodovani rsa!'
    echo 'Failed'
    result='Failed'
  fi
else
  printf 'Bad chunks count in encrypted data (expected 2, given %s) !\n' "$chunkCount"
  result='Failed'
fi
rm -f test1a.conf.sample test1a.conf.out test1a.conf

echo
echo "Test apostrofu v promenne (encoding):"
if "${compileConfEncrypt}" --rsa -k test1.rsa.key <<< "hokus'a"; then
  echo 'Chyba apostrofu v promenne (encoding)!'
  result='Failed'
else
  echo 'Ok'
fi

echo
echo "Test uvozovky v promenne (encoding):"
if "${compileConfEncrypt}" --rsa -k test1.rsa.key <<< 'hokus"a'; then
  echo 'Chyba uvozovky v promenne (encoding)!'
  result='Failed'
else
  echo 'Ok'
fi

echo
echo "Test apostrofu v promenne (decoding):"
if "${compileConf}" -K test1.rsa.key.priv production test1.conf.apost.sample test1.conf.apost; then
  echo 'Chyba apostrofu v promenne (decoding)!'
  result='Failed'
else
  echo 'Ok'
fi

echo
echo "Test uvozovky v promenne (decoding):"
if "${compileConf}" -K test1.rsa.key.priv production test1.conf.quote.sample test1.conf.quote; then
  echo 'Chyba uvozovky v promenne (decoding)!'
  result='Failed'
else
  echo 'Ok'
fi

printf '\n\n====== Souhrn ======\n'
if [[ "$result" == 'Ok' ]]; then
  printf 'Zadny z testu neselhal.\n\n'
else
  printf 'Aspon jeden test selhal!\n\n'
  exit 1
fi
