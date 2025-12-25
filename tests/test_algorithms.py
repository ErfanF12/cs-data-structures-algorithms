from algorithms.searching import linear_search, binary_search
from algorithms.sorting import bubble_sort, merge_sort, quick_sort
from algorithms.graph_traversal import bfs, dfs


def run_tests():
    # Searching tests
    arr = [5, 2, 9, 1]
    assert linear_search(arr, 9) == 2
    assert linear_search(arr, 100) == -1

    sorted_arr = [1, 2, 5, 9]
    assert binary_search(sorted_arr, 5) == 2
    assert binary_search(sorted_arr, 7) == -1

    # Sorting tests
    arr2 = [3, 1, 4, 2]
    assert bubble_sort(arr2.copy()) == [1, 2, 3, 4]
    assert merge_sort(arr2.copy()) == [1, 2, 3, 4]
    assert quick_sort(arr2.copy()) == [1, 2, 3, 4]

    # Graph traversal tests
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],
        "D": []
    }
    assert bfs(graph, "A") == ["A", "B", "C", "D"]
    assert dfs(graph, "A") == ["A", "B", "D", "C"]

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
