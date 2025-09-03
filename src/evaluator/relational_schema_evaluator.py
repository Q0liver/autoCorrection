import parser.relational_schema_parser.fd_bases_and_key_parser as fdp
import parser.relational_schema_parser.relational_schema_parser as rsp
import parser.simple_structure_parser.simple_structure_parser as ssp

sub="""Min=0 
Max=m"""

ref="""Max=m
Min=0 
"""

def parse(string, func_list):
    for func in func_list:
        try:
            pString = func(string)
            break
        except:
            pass
    else:
        print("nicht parsbar:")
        print(string)
    return pString

def compare(sub, ref, func=lambda x:x):
    refs = [func(line) for line in ref.splitlines()]
    for line in sub.splitlines():
        if func(line) not in refs:
            print("nicht gefunden:")
            print(line)
    print("done")
#compare(sub, ref, fdp.functional_dependencies_parser)
#compare(sub, ref, rsp.relational_schema_parser)
#compare(sub, ref, fdp.membership_test_parser)
#compare(sub, ref, lambda line: parse(line, (fdp.functional_dependencies_parser,rsp.relational_schema_parser,ssp.set_parser)))
compare(sub, ref, lambda x:x)