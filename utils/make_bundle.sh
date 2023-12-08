cd $(dirname "$0")
rm bundle.zip
mkdir tmp

cd ../scoring_program
zip -r ../utils/tmp/scoring_program.zip *

cd ../reference_test
zip -r ../utils/tmp/reference_test.zip *

cd ../reference_valid
zip -r ../utils/tmp/reference_valid.zip *

# cd ../starting_kit
# cp -r ../scoring_program ./ 
# zip -r ../utils/tmp/starting_kit.zip *
# rm -rf scoring_program

cd ..
cp -r competition.yaml pages logo.png utils/tmp/

cd utils/tmp
zip -r ../bundle.zip *
cd ..
rm -rf tmp