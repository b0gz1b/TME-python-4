#============================================#
# UE Calculabilite L3                        #
# TME GHC propres                            #
# Mathieu.Jaume@lip6.fr                      #
#============================================#

from reduced_ghc import *


# Symboles annulables
# -------------------

def canc0(r):
    # r : liste de productions
    def is_empty_list(l):
        return len(l)==0
    return [s for s,ls in r if exists_such_that(ls,is_empty_list)]

def next_canc(r,eqnt,prev):
    # r : liste de productions
    # eqnt : egalite sur les non terminaux
    # prev : liste de non terminaux de depart
    # A COMPLETER
    return

def canc(r,eqnt):
    # r : liste de productions
    # eqnt : egalite sur les non terminaux
    def _next_canc(e):
        return next_canc(r,eqnt,e)
    return fixpoint_from(make_eq_set(eqnt),_next_canc,canc0(r))

# Elimination des epsilon-productions
# -----------------------------------

def remove_eps_prod(g):
    # g : ghc
    nt,t,r,si,eqnt = g
    canc_g = canc(r,eqnt)
    def make_new_prod(l):
        if len(l)==0:
            return [[]]
        else:
            res_rec = make_new_prod(l[1:])
            add_first = [[l[0]]+lrec for lrec in res_rec]
            if is_in(eqnt,l[0],canc_g):
                acc = add_first + res_rec
            else:
                acc = add_first
            return acc
    def make_new_prods(ls):
        res = []
        for l in ls:
            new_l = [x for x in make_new_prod(l) if len(x)>0]
            res = union(make_eq_prod(nt,eqnt),new_l,res)
        return res
    new_r = [(s,make_new_prods(ls)) for s,ls in r]
    return (nt,t,new_r,si,eqnt) 

# Egalite sur les paires de symboles non-terminaux

def make_eq_pair_nt(eqnt):
    # eqnt :  egalite sur les non terminaux
    def _eq_pair_nt(p1,p2):
        x1,y1 = p1
        x2,y2 = p2
        return eqnt(x1,x2) and eqnt(y1,y2)
    return _eq_pair_nt


# Paires unitaires
# ----------------

def unit_pair0(nt,r,eqnt):
    # nt : symboles non terminaux
    # r : liste de productions
    # eqnt : egalite sur les non terminaux
    # A COMPLETER
    return

def next_unit_pair(nt,r,eqnt,prev):
    # nt : symboles non terminaux
    # r : liste de productions
    # eqnt : egalite sur les non terminaux
    # prev : liste de non terminaux de depart
    # A COMPLETER
    return

def unit_pair(nt,r,eqnt):
    # nt : symboles non terminaux
    # r : liste de productions
    # eqnt : egalite sur les non terminaux
    def _next_unit_pair(e):
        return next_unit_pair(nt,r,eqnt,e)
    return fixpoint_from(make_eq_set(make_eq_pair_nt(eqnt)),\
                         _next_unit_pair,unit_pair0(nt,r,eqnt))


# Elimination des paires unitaires
# --------------------------------

def remove_unit_pairs(g):
    # g : ghc
    # A COMPLETER
    return

# Construction d'une grammaire propre
# -----------------------------------

def make_gp(g):
    # g : ghc
    return remove_unit_pairs(remove_eps_prod(reduce_grammar(g)))
