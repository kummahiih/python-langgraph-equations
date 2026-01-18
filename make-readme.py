import langgraph_equations  

README = langgraph_equations.get_primitives.__doc__
with open('README.md', 'wt') as readme_file:
    readme_file.write(README)
