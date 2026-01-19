import langgraph_equations  

module_doc = langgraph_equations.__doc__
get_primitives_documentation  = langgraph_equations.get_primitives.__doc__
simplify_doc = langgraph_equations.__simplify_doc__
with open('README.md', 'wt') as readme_file:
    readme_file.write(module_doc)
    readme_file.write("\n")
    readme_file.write("\n")
    readme_file.write(get_primitives_documentation)
    readme_file.write("\n")
    readme_file.write(simplify_doc)
    readme_file.write("\n")

