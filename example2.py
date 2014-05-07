import jinja2
import os

THIS_DIR = os.path.abspath(os.path.dirname(__file__))

templateLoader = jinja2.FileSystemLoader( searchpath=THIS_DIR )
templateEnv = jinja2.Environment( loader=templateLoader )

TEMPLATE_FILE = "example2.html"
template = templateEnv.get_template( TEMPLATE_FILE )

# Here we add a new input variable containing a list.
# Its contents will be expanded in the HTML as a unordered list.
FAVORITES = [ "chocolates", "lunar eclipses", "rabbits" ]

templateVars = { "title" : "Test Example",
                 "description" : "A simple inquiry of function.",
                 "favorites" : FAVORITES
               }

#outputText = template.render( templateVars )

# Output file
html_filename = os.path.join(THIS_DIR, "index2.html")
template.stream(templateVars).dump(html_filename)