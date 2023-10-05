from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State

q0 = State("q0")
q1 = State("q1")
q2 = State("q2")
q3 = State("q3")
q4 = State("q4")
q5 = State("q5")
q6 = State("q6")
q7 = State("q7")
q8 = State("q8")
q9 = State("q9")
q10 = State("q10")
q11 = State("q11")
q12 = State("q12")
q13 = State("q13")
q14 = State("q14")
q15 = State("q15")
q16 = State("q16")
q17 = State("q17")
q18 = State("q18")
q19 = State("q19")
q20 = State("q20")
q21 = State("q21")
q22 = State("q22")
q23 = State("q23")
q24 = State("q24")
q25 = State("q25")
q26 = State("q26")
q27 = State("q27")
q28 = State("28")
q29 = State("q29")
q30 = State("q30")
q31 = State("q31")
q32 = State("q32")
q33 = State("q33")
q34 = State("q34")
q35 = State("q35")
q36 = State("q36")
q37 = State("q37")
q38 = State("q38")
q39 = State("q39")
q40 = State("q40")
q41 = State("q41")
q42 = State("q42")
q43 = State("q43")
q44 = State("q44")
q45 = State("q45")
q46 = State("q46")
q47 = State("q47")

dfa = DeterministicFiniteAutomaton(
states={q0, q1, q2, q3, q4, q5, q6, q7},
input_symbols={"1", "2","3"},
start_state=q0,
final_states={q31,q32,q33,q34,q35,q36,q37,q38,q39,q40,q42,q43,q46,q47} # Define the set of accepting states
)

dfa.add_transitions([

(q0,"1",q1),
(q0,"2",q1),

(q1,"1",q3),
(q1,"2",q4),

(q2,"1",q5),
(q2,"2",q6),

(q3,"1",q7),
(q3,"2",q9),

(q7,"1",q15),
(q7,"2",q16),

(q8,"1",q17),
(q8,"2",q18),

(q4,"1",q9),
(q4,"2",q10),

(q9,"1",q19),
(q9,"2",q20),

(q10,"1",q21),
(q10,"2",q22),

(q5,"1",q11),
(q5,"2",q12),

(q11,"1",q23),
(q11,"2",q24),

(q12,"1",q25),
(q12,"2",q26),

(q6,"1",q13),
(q6,"2",q14),

(q13,"1",q27),
(q13,"2",q28),

(q14,"1",q29),
(q14,"2",q30),

(q15,"1",q27),
(q15,"2",q17),

(q16,"1",q31),
(q16,"2",q17),

(q17,"1",q32),
(q17,"2",q33),

(q18,"1",q32),
(q18,"2",q26),

(q19,"1",q34),
(q19,"2",q43),

(q20,"1",q35),
(q20,"2",q30),

(q21,"1",q36),

(q22,"1",q35),
(q22,"2",q37),

(q23,"1",q38),
(q23,"2",q39),

(q24,"1",q38),
(q24,"2",q39),

(q25,"1",q40),
(q25,"2",q47),

(q26,"1",q44),
(q26,"2",q47),

(q27,"1",q41),
(q27,"2",q44),

(q28,"1",q42),
(q28,"2",q43),

(q29,"1",q43),
(q29,"2",q44),

(q30,"1",q44),
(q30,"2",q47),

(q41,"1",q44),

(q44,"1",q45),
(q44,"2",q46),

(q45,"1",q46),
])