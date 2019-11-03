npm run build

sed -i -e 's#css/theme/night.css#css/theme/beige.css#g' src/index.html
sed -i -e 's#build/styles/agate.min.css#build/styles/zenburn.min.css#g' src/index.html

npm run build:contrast

sed -i -e 's#css/theme/beige.css#css/theme/night.css#g' src/index.html
sed -i -e 's#build/styles/zenburn.min.css#build/styles/agate.min.css#g' src/index.html
