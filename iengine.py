from kb import KnowledgeBase
from tt import TruthTable
from bc import BackwardChaining
from fc import ForwardChaining
from parse_file import KB_DATA
# from converter import convert_to_horn_clauses


data = KB_DATA()
clauses = data.TellData()
# clauses = ["p2 => p3", "p3 => p1", "c => e", "b&e => f", "f&g => h", "p2&p1&p3 => d", "p1&p3 => c", "a", "b", "p2"]
query_data = data.QueryData()
# instantiate KB instance
kb = KnowledgeBase(clauses)


match data.getMethod():
    case "BC":
        # instantiate BV instance using KB
        bc = BackwardChaining(kb)
        # query the kb using backward chaining to check if 'd' can be proven
        result, proven = bc.query(query_data)
        # print the result
        print("Backward Chaining result:", "YES: " + ', '.join(proven) if result else "NO")

    case "TT":
        # create a TruthTable instance using the same knowledge base
        tt = TruthTable(kb)
        # query the knowledge base using the truth table method to check if 'd' is entailed by the KB
        result = tt.query(query_data)
        # print the result
        print("Truth Table result:", result)

    case "FC":
        # instantiate the FC using KB
        fc = ForwardChaining(kb)
        # query the KB using forward chaining to check if 'd' can be proven
        result, derived = fc.query(query_data)
        # print the result
        print("Forward Chaining result:", "YES: " + ', '.join(derived) if result else "NO")
