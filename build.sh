# python3.8 -m pip install --target .backend/libraries -r backend/requirements.txt
cd backend/libraries/
zip -r9 ../lambda.zip .
cd ..
zip -g ./lambda.zip *.py

# cd ../frontend
# npm run build
