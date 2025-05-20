// 1

let rec replace listParam origVal newVal =
    match listParam with
    | [] -> []
    | first :: rest ->
        let newFirst = if first = origVal then newVal else first
        newFirst :: replace rest origVal newVal

// 2
let rec mergeList listA listB =
    match (listA, listB) with
    | ([], []) -> []
    | ([], listBnotempty) -> listBnotempty
    | (listAnotempty, []) -> listAnotempty
    | (listAFirst::listAnotempty, listBFirst::listBnotempty) -> listAFirst :: listBFirst :: mergeList listAnotempty listBnotempty

// 3
type BST =
    | Empty
    | TreeNode of int * BST * BST

let rec insertFunc valueParam treeParam  =
    match treeParam  with
    | Empty -> TreeNode(valueParam, Empty, Empty)
    | TreeNode(v, left, right) ->
        if valueParam = v then treeParam 
        else if valueParam < v then TreeNode(v, insertFunc valueParam left, right)
        else TreeNode(v, left, insertFunc valueParam right)

let rec searchFunc valueParam treeParam  =
    match treeParam  with
    | Empty -> false
    | TreeNode(v, left, right) ->
        if valueParam = v then true
        else if valueParam < v then searchFunc valueParam left
        else searchFunc valueParam right

let rec countFunc boolFuncParam treeParam  =
    match treeParam  with
    | Empty -> 0
    | TreeNode(v, left, right) ->
        let thisV = if boolFuncParam v then 1 else 0 // boolean
        thisV + countFunc boolFuncParam left + countFunc boolFuncParam right

let evenCount treeParam  = countFunc (fun x -> x % 2 = 0) treeParam 
