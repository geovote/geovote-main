# =============================================
#  Helper that describes all functionalities
# =============================================

if [[ $# -eq 0 ]] || [[ "$1" == "-h" ]]; then
    echo "$(basename "$0") [-h] [-e env -b backend c] -- program to deal with the ecosystem
where:
    -p  the path of the flask application"
    exit 0
fi

# =============================================
#  PATH
# =============================================

if [[ $# -eq 0 ]] || [[ "$1" == "-p" ]]; then
  FLASK_PATH=$2
fi

# =============================================
#  execute
# =============================================

yarn build
mkdir -p $FLASK_PATH/static/css;
mkdir -p $FLASK_PATH/static/icons;
mkdir -p $FLASK_PATH/static/js;
rm -f $FLASK_PATH/static/css/main.*.chunk.css
rm -f $FLASK_PATH/static/css/main.*.chunk.css.map
rm -f $FLASK_PATH/static/js/main.*.chunk.js
rm -f $FLASK_PATH/static/js/main.*.chunk.js.map
cp -r build/static/css $FLASK_PATH/static;
cp -r build/icons $FLASK_PATH/static;
cp -r build/static/js $FLASK_PATH/static;
cp build/index.html $FLASK_PATH/templates/bundle.jinja;
