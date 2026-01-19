if __name__ == '__main__':
    import doctest
    import langgraph_equations

    # by importing these here, there might be some import errors left..
    globs = {
        'get_primitives': langgraph_equations.get_primitives
    }
    
    doctest.testfile(filename="get_primitives.py", module_relative=True, package=langgraph_equations, globs=globs)
    doctest.testfile(filename="simplify.py", module_relative=True, package=langgraph_equations, globs=globs)


    