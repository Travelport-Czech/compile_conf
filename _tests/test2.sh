#!/usr/bin/env bash
result='Ok'

function checkResult() {
   local stage="$1"
   read -r firstline < test.stages.conf
    
   if [[ "$stage" == "$firstline" ]]; then
     echo "$stage OK" 
   else
     echo "$stage Failed" 
     cat test.stages.conf
     result='Failed'
   fi
   rm -f test.stages.conf
}

echo "Test config is generated correctly for all stages:"
for stage in production testing internal support devel robots pipeline; do
   ../compile_conf "${stage}" test.stages.conf.sample test.stages.conf
   checkResult "${stage}"
done

../compile_conf -T X test.stages.conf.sample test.stages.conf
checkResult 'custom'

printf '\n\n====== Summary ======\n'
if [[ "$result" == 'Ok' ]]; then
  printf 'Everything is OK.\n\n'
else
  printf 'At least one test has failed!\n\n'
  exit 1
fi
