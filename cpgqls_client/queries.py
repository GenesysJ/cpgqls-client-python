
def import_code_query(path, project_name=None, language=None):
    if not path:
        raise Exception('An importCode query requires a project path')
    if project_name and language:
        fmt_str = u"""importCode(inputPath=\"%s\", projectName=\"%s\",
language=\"%s\")"""
        return fmt_str % (path, project_name, language)
    if project_name and (language is None):
        fmt_str = u"""importCode(inputPath=\"%s\", projectName=\"%s\")"""
        return fmt_str % (path, project_name)
    return u"importCode(\"%s\")" % (path)


def open_query(project_name):
    return f"open(\"{project_name}\")"


def close_query(project_name):
    return f"close(\"{project_name}\")"


def delete_query(project_name):
    return f"delete(\"{project_name}\")"


def help_query():
    return f"help"


def workspace_query():
    return "workspace"


def project_query():
    return "project"

def get_AST_graph(project_name):
    return f"cpg.method.name(\"{project_name}\").dotAst.headOption.getOrElse(\"No AST found for this method\")"


def get_CFG_graph(project_name):
    return f"cpg.method.name(\"{project_name}\").dotCfg.headOption.getOrElse(\"No CFG found for this method\")"

def get_CDG_graph(project_name):
    return f"cpg.method.name(\"{project_name}\").dotCdg.headOption.getOrElse(\"No CDG found for this method\")"

def get_DDG_graph(project_name):
    return f"cpg.method.name(\"{project_name}\").dotDdg.headOption.getOrElse(\"No DDG found for this method\")"

def get_PDG_graph(project_name):
    return f"cpg.method.name(\"{project_name}\").dotPdg.headOption.getOrElse(\"No PDG found for this method\")"

def get_CPG14_graph(project_name):
    return f"cpg.method.name(\"{project_name}\").dotCpg14.headOption.getOrElse(\"No CPG14 found for this method\")"

def get_ALL_graph(project_name):
    return f"cpg.method.name(\"{project_name}\").dotAll.headOption.getOrElse(\"No ALL found for this method\")"

def import_string_function_query(function: str) -> str:
    return f'importCode.c.fromString("""{function}""")'

def help_cpg():
    return f"cpg.help"
