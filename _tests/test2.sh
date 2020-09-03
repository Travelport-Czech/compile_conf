#!/usr/bin/env bash
result='Ok'

echo "Test config is generated correctly for all stages:"
for stage in production testing internal support devel robots pipeline; do
   ../compile_conf "${stage}" test.stages.conf.sample test.stages.conf
   read -r firstline < test.stages.conf
    
   if [[ "$stage" == "$firstline" ]]; then
     echo "$stage OK" 
   else
     echo "$stage Failed" 
     cat test.stages.conf
     result='Failed'
   fi
   rm -f test.stages.conf
done

printf '\n\n====== Summary ======\n'
if [[ "$result" == 'Ok' ]]; then
  printf 'Everything is OK.\n\n'
else
  printf 'At least one test has failed!\n\n'
  exit 1
fi
