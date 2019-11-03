npm run build

sed -i -e 's#css/theme/night.css#css/theme/beige.css#g' src/index.html
sed -i -e 's#lib/css/monokai.css#lib/css/zenburn.css#g' src/index.html

npm run build:contrast

sed -i -e 's#css/theme/beige.css#css/theme/night.css#g' src/index.html
sed -i -e 's#lib/css/zenburn.css#lib/css/monokai.css#g' src/index.html
