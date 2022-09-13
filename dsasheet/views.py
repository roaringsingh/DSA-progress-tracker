from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.core import exceptions
from .models import *


# Create your views here.

@login_required()
def array(request):
    if request.POST:
        data = arrays.Array.objects.get(uid=request.user)
        for i in request.POST.keys():
            if i == 'csrfmiddlewaretoken':
                continue
            setattr(data, i, request.POST[i])
        data.save()
    data = arrays.Array.objects.get(uid=request.user)
    tempdata = list(ArrayForm(instance=data))
    k = 1

    easyques = {
        1: ['https://leetcode.com/problems/two-sum/', 'Two Sum'],
        2: ['https://leetcode.com/problems/best-time-to-buy-and-sell-stock/', 'Best Time To Buy And Sell Stock'],
        3: ["https://leetcode.com/problems/plus-one/", 'Plus One'],
        4: ["https://leetcode.com/problems/move-zeroes/", 'Move Zeroes'],
        5: ["https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/", 'Best Time To Buy And Sell Stock II'],
        6: ["https://leetcode.com/problems/running-sum-of-1d-array/", 'Running Sum Of 1D Array'],
        7: ["https://leetcode.com/problems/find-pivot-index/", 'Find Pivot Index'],
        8: ["https://leetcode.com/problems/majority-element/", 'Majority Element'],
        9: ["https://leetcode.com/problems/fibonacci-number/", 'Fibonacci Number'],
        10: ["https://leetcode.com/problems/squares-of-a-sorted-array/", 'Squares Of A Sorted Array'],
        11: ["https://leetcode.com/problems/pascals-triangle/", 'Pascals Triangle'],
        12: ["https://leetcode.com/problems/remove-duplicates-from-sorted-array/",
             'Remove Duplicates From Sorted Array']
    }
    for i in range(1, 13):
        easyques[i].extend(tempdata[k:k + 4])
        k = k + 4

    medques = {
        1: ['https://leetcode.com/problems/merge-intervals/', 'Merge Intervals'],
        2: ['https://leetcode.com/problems/3sum/', '3Sum'],
        3: ['https://leetcode.com/problems/product-of-array-except-self/', 'Product Of Array Except Self'],
        4: ['https://leetcode.com/problems/insert-delete-getrandom-o1/', 'Insert Delete Getrandom O1'],
        5: ['https://leetcode.com/problems/subarray-sum-equals-k/', 'Subarray Sum Equals K'],
        6: ['https://leetcode.com/problems/next-permutation/', 'Next Permutation'],
        7: ['https://leetcode.com/problems/spiral-matrix/', 'Spiral Matrix'],
        8: ['https://leetcode.com/problems/container-with-most-water/', 'Container With Most Water'],
        9: ['https://leetcode.com/problems/rotate-image/', 'Rotate Image'],
        10: ['https://leetcode.com/problems/word-search/', 'Word Search'],
        11: ['https://leetcode.com/problems/3sum-closest/', '3Sum Closest'],
        12: ['https://leetcode.com/problems/game-of-life/', 'Game Of Life'],
        13: ['https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/',
             'Pairs Of Songs With Total Durations Divisible By 60'],
        14: ['https://leetcode.com/problems/4sum/', '4Sum'],
        15: ['https://leetcode.com/problems/find-the-duplicate-number/', 'Find The Duplicate Number'],
        16: ['https://leetcode.com/problems/combination-sum/', 'Combination Sum'],
        17: ['https://leetcode.com/problems/jump-game-ii/', 'Jump Game Ii'],
        18: ['https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/',
             'Maximum Points You Can Obtain From Cards'],
        19: ['https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/',
             'Maximum Area Of A Piece Of Cake After Horizontal And Vertical Cuts'],
        20: ['https://leetcode.com/problems/max-area-of-island/', 'Max Area Of Island'],
        21: ['https://leetcode.com/problems/find-all-duplicates-in-an-array/',
             'Find All Duplicates In An Array'],
        22: ['https://leetcode.com/problems/k-diff-pairs-in-an-array/', 'K Diff Pairs In An Array'],
        23: ['https://leetcode.com/problems/subsets/', 'Subsets'],
        24: ['https://leetcode.com/problems/invalid-transactions/', 'Invalid Transactions'],
        25: ['https://leetcode.com/problems/jump-game/', 'Jump Game'],
        26: ['https://leetcode.com/problems/subarray-sums-divisible-by-k/', 'Subarray Sums Divisible By K']
    }
    for i in range(1, 27):
        medques[i].extend(tempdata[k:k + 4])
        k = k + 4

    hardques = {
        1: ['https://leetcode.com/problems/first-missing-positive/', 'First Missing Positive'],
        2: ['https://leetcode.com/problems/largest-rectangle-in-histogram/', 'Largest Rectangle In Histogram'],
        3: ['https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/',
            'Insert Delete Get Random 01 Duplicates Allowed'],
        4: ['https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/',
            'Best Time To Buy And Sell Stock III'],
        5: ['https://leetcode.com/problems/max-value-of-equation/', 'Max Value Of Equation']
    }
    for i in range(1, 6):
        hardques[i].extend(tempdata[k:k + 4])
        k = k + 4

    context = {
        'easyques': easyques,
        'medques': medques,
        'hardques': hardques,
    }
    return render(request, 'sheet/Arrays.html', context)


@login_required()
def math(request):
    if request.POST:
        data = maths.Maths.objects.get(uid=request.user)
        for i in request.POST.keys():
            if i == 'csrfmiddlewaretoken':
                continue
            setattr(data, i, request.POST[i])
        data.save()
    data = maths.Maths.objects.get(uid=request.user)
    tempdata = list(MathsForm(instance=data))
    k = 1

    # Mathematics
    measyques = {
        1: ['https://leetcode.com/problems/reverse-integer/', 'Reverse Integer'],
        2: ['https://leetcode.com/problems/add-binary/', 'Add Binary'],
        3: ['https://leetcode.com/problems/palindrome-number/', 'Palindrome Number'],
        4: ['https://leetcode.com/problems/minimum-moves-to-equal-array-elements/',
            'Minimum Moves To Equal Array Elements'],
        5: ['https://leetcode.com/problems/happy-number/', 'Happy Number'],
        6: ['https://leetcode.com/problems/excel-sheet-column-title/', 'Excel Sheet Column Title'],
        7: ['https://leetcode.com/problems/missing-number/', 'Missing Number'],
        8: ['https://leetcode.com/problems/maximum-product-of-three-numbers/',
            'Maximum Product Of Three Numbers'],
        9: ['https://leetcode.com/problems/power-of-two/', 'Power Of Two']
    }
    for i in range(1, 10):
        measyques[i].extend(tempdata[k:k + 4])
        k = k + 4

    mmedques = {
        1: ['https://leetcode.com/problems/encode-and-decode-tinyurl/', 'Encode And Decode TinyURL'],
        2: ['https://leetcode.com/problems/string-to-integer-atoi/', 'String To Integer AtoI'],
        3: ['https://leetcode.com/problems/multiply-strings/', 'Multiply Strings'],
        4: ['https://leetcode.com/problems/angle-between-hands-of-a-clock/', 'Angle Between Hands Of A Clock'],
        5: ['https://leetcode.com/problems/integer-break/', 'Integer Break'],
        6: ['https://leetcode.com/problems/valid-square/', 'Valid Square'],
        7: ['https://leetcode.com/problems/the-kth-factor-of-n/', 'The Kth Factor Of N']
    }
    for i in range(1, 8):
        mmedques[i].extend(tempdata[k:k + 4])
        k = k + 4

    mhardques = {
        1: ['https://leetcode.com/problems/basic-calculator/', 'Basic Calculator'],
        2: ['https://leetcode.com/problems/max-points-on-a-line/', 'Max Points On A Line'],
        3: ['https://leetcode.com/problems/permutation-sequence/', 'Permutation Sequence'],
        4: ['https://leetcode.com/problems/number-of-digit-one/', 'Number Of Digit One']
    }
    for i in range(1, 5):
        mhardques[i].extend(tempdata[k:k + 4])
        k = k + 4

    # Greedy
    gmedques = {
        1: ['https://leetcode.com/problems/task-scheduler/', 'Task Scheduler'],
        2: ['https://leetcode.com/problems/gas-station/', 'Gas Station'],
        3: ['https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/',
            'Minimum Deletion Cost To Avoid Repeating Letters'],
        4: ['https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/',
            'Maximum Number Of Events That Can Be Attended'],
        5: ['https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/',
            'Minimum Deletions To Make Character Frequencies Unique'],
        6: ['https://leetcode.com/problems/remove-k-digits/', 'Remove K Digits'],
        7: ['https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/',
            'Restore The Array From Adjacent Pairs'],
        8: ['https://leetcode.com/problems/non-overlapping-intervals/', 'Non Overlapping Intervals']
    }
    for i in range(1, 9):
        gmedques[i].extend(tempdata[k:k + 4])
        k = k + 4

    ghardques = {
        1: ['https://leetcode.com/problems/candy/', 'Candy'],
        2: ['https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/',
            'Minimum Number Of Taps To Open To Water A Garden'],
        3: ['https://leetcode.com/problems/create-maximum-number/', 'Create Maximum Number']
    }
    for i in range(1, 4):
        ghardques[i].extend(tempdata[k:k + 4])
        k = k + 4

    context = {
        'measyques': measyques,
        'mmedques': mmedques,
        'mhardques': mhardques,
        'gmedques': gmedques,
        'ghardques': ghardques,
    }
    return render(request, 'sheet/Maths.html', context)


@login_required()
def stack(request):
    if request.POST:
        data = stacks.Stack.objects.get(uid=request.user)
        for i in request.POST.keys():
            if i == 'csrfmiddlewaretoken':
                continue
            setattr(data, i, request.POST[i])
        data.save()
    data = stacks.Stack.objects.get(uid=request.user)
    tempdata = list(StackForm(instance=data))
    k = 1

    # Two Pointer
    tpques = {
        1: ['https://leetcode.com/problems/partition-labels/', 'Partition Labels'],
        2: ['https://leetcode.com/problems/sort-colors/', 'Sort Colors'],
        3: ['https://leetcode.com/problems/longest-repeating-character-replacement/',
            'Longest Repeating Character Replacement'],
        4: ['https://leetcode.com/problems/maximum-number-of-visible-points/', 'Maximum Number Of Visible Points'],
        5: ['https://leetcode.com/problems/subarrays-with-k-different-integers/', 'Subarrays With K Different Integers']
    }
    for i in range(1, 6):
        tpques[i].extend(tempdata[k:k + 4])
        k = k + 4

    # Sliding Window
    swques = {
        1: ['https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/',
            'Longest Substring With At Least K Repeating Characters'],
        2: ['https://leetcode.com/problems/max-consecutive-ones-iii/', 'Max Consecutive Ones Iii'],
        3: ['https://leetcode.com/problems/grumpy-bookstore-owner/', 'Grumpy Bookstore Owner'],
        4: ['https://leetcode.com/problems/sliding-window-median/', 'Sliding Window Median']
    }
    for i in range(1, 5):
        swques[i].extend(tempdata[k:k + 4])
        k = k + 4

    # Stack
    seasyques = {
        1: ['https://leetcode.com/problems/min-stack/', 'Min Stack'],
        2: ['https://leetcode.com/problems/next-greater-element-i/', 'Next Greater Element I'],
        3: ['https://leetcode.com/problems/backspace-string-compare/', 'Backspace String Compare'],
        4: ['https://leetcode.com/problems/implement-queue-using-stacks/', 'Implement Queue Using Stacks'],
        5: ['https://leetcode.com/problems/implement-stack-using-queues/', 'Implement Stack Using Queues']
    }
    for i in range(1, 6):
        seasyques[i].extend(tempdata[k:k + 4])
        k = k + 4

    smedques = {
        1: ['https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/',
            'Remove All Adjacent Duplicates In String Ii'],
        2: ['https://leetcode.com/problems/daily-temperatures/', 'Daily Temperatures'],
        3: ['https://leetcode.com/problems/flatten-nested-list-iterator/', 'Flatten Nested List Iterator'],
        4: ['https://leetcode.com/problems/online-stock-span/', 'Online Stock Span'],
        5: ['https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/', 'Minimum Cost Tree From Leaf Values'],
        6: ['https://leetcode.com/problems/sum-of-subarray-minimums/', 'Sum Of Subarray Minimums'],
        7: ['https://leetcode.com/problems/evaluate-reverse-polish-notation/', 'Evaluate Reverse Polish Notation']
    }
    for i in range(1, 8):
        smedques[i].extend(tempdata[k:k + 4])
        k = k + 4

    context = {
        'tpques': tpques,
        'swques': swques,
        'seasyques': seasyques,
        'smedques': smedques,
    }
    return render(request, 'sheet/Stack.html', context)


def hashing(request):
    if request.POST:
        data = hash.Hash.objects.get(uid=request.user)
        for i in request.POST.keys():
            if i == 'csrfmiddlewaretoken':
                continue
            setattr(data, i, request.POST[i])
        data.save()
    data = hash.Hash.objects.get(uid=request.user)
    tempdata = list(HashForm(instance=data))
    k = 1

    # Hash Table
    heasyques = {
        1: ['https://leetcode.com/problems/verifying-an-alien-dictionary/', 'Verifying An Alien Dictionary'],
        2: ['https://leetcode.com/problems/design-hashmap/', 'Design Hashmap']
    }
    for i in range(1, 3):
        heasyques[i].extend(tempdata[k:k + 4])
        k = k + 4

    hmedques = {
        1: ['https://leetcode.com/problems/top-k-frequent-elements/', 'Top K Frequent Elements'],
        2: ['https://leetcode.com/problems/design-twitter/', 'Design Twitter']
    }
    for i in range(1, 3):
        hmedques[i].extend(tempdata[k:k + 4])
        k = k + 4

    # Binary Search
    beasyques = {
        1: ['https://leetcode.com/problems/sqrtx/', 'Sqrtx'],
        2: ['https://leetcode.com/problems/binary-search/', 'Binary Search'],
        3: ['https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/',
            'Count Negative Numbers In A Sorted Matrix'],
        4: ['https://leetcode.com/problems/peak-index-in-a-mountain-array/', 'Peak Index In A Mountain Array']
    }
    for i in range(1, 5):
        beasyques[i].extend(tempdata[k:k + 4])
        k = k + 4

    bmedques = {
        1: ['https://leetcode.com/problems/time-based-key-value-store/', 'Time Based Key Value Store'],
        2: ['https://leetcode.com/problems/search-in-rotated-sorted-array/', 'Search In Rotated Sorted Array'],
        3: ['https://leetcode.com/problems/powx-n/', 'Powx N'],
        4: ['https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/',
            'Find First And Last Position Of Element In Sorted Array'],
        5: ['https://leetcode.com/problems/find-peak-element/', 'Find Peak Element'],
        6: ['https://leetcode.com/problems/search-a-2d-matrix/', 'Search A 2D Matrix'],
        7: ['https://leetcode.com/problems/divide-two-integers/', 'Divide Two Integers'],
        8: ['https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/',
            'Capacity To Ship Packages Within D Days'],
        9: ['https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/', 'Minimum Limit Of Balls In A Bag']
    }
    for i in range(1, 10):
        bmedques[i].extend(tempdata[k:k + 4])
        k = k + 4

    bhardques = {
        1: ['https://leetcode.com/problems/median-of-two-sorted-arrays/', 'Median Of Two Sorted Arrays'],
        2: ['https://leetcode.com/problems/count-of-smaller-numbers-after-self/',
            'Count Of Smaller Numbers After Self'],
        3: ['https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/',
            'Max Sum Of Rectangle No Larger Than K'],
        4: ['https://leetcode.com/problems/split-array-largest-sum/', 'Split Array Largest Sum'],
        5: ['https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/',
            'Shortest Subarray With Sum At Least K']
    }
    for i in range(1, 6):
        bhardques[i].extend(tempdata[k:k + 4])
        k = k + 4

    context = {
        'heasyques': heasyques,
        'hmedques': hmedques,
        'beasyques': beasyques,
        'bmedques': bmedques,
        'bhardques': bhardques,
    }
    return render(request, 'sheet/Hash.html', context)


def string(request):
    if request.POST:
        data = strings.String.objects.get(uid=request.user)
        for i in request.POST.keys():
            if i == 'csrfmiddlewaretoken':
                continue
            setattr(data, i, request.POST[i])
        data.save()
    data = strings.String.objects.get(uid=request.user)
    tempdata = list(StringForm(instance=data))
    k = 1

    easyques = {
        1: ['https://leetcode.com/problems/add-strings/', 'Add Strings'],
        2: ['https://leetcode.com/problems/longest-common-prefix/', 'Longest Common Prefix'],
        3: ['https://leetcode.com/problems/valid-palindrome-ii/', 'Valid Palindrome Ii'],
        4: ['https://leetcode.com/problems/roman-to-integer/', 'Roman To Integer'],
        5: ['https://leetcode.com/problems/implement-strstr/', 'Implement Strstr']
    }
    for i in range(1, 6):
        easyques[i].extend(tempdata[k:k + 4])
        k = k + 4

    medques = {
        1: ['https://leetcode.com/problems/longest-substring-without-repeating-characters/',
            'Longest Substring Without Repeating Characters'],
        2: ['https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/',
            'Minimum Remove To Make Valid Parentheses'],
        3: ['https://leetcode.com/problems/longest-palindromic-substring/', 'Longest Palindromic Substring'],
        4: ['https://leetcode.com/problems/group-anagrams/', 'Group Anagrams'],
        5: ['https://leetcode.com/problems/generate-parentheses/', 'Generate Parentheses'],
        6: ['https://leetcode.com/problems/basic-calculator-ii/', 'Basic Calculator Ii'],
        7: ['https://leetcode.com/problems/integer-to-roman/', 'Integer To Roman'],
        8: ['https://leetcode.com/problems/reverse-words-in-a-string/', 'Reverse Words In A String'],
        9: ['https://leetcode.com/problems/simplify-path/', 'Simplify Path'],
        10: ['https://leetcode.com/problems/zigzag-conversion/', 'Zigzag Conversion']
    }
    for i in range(1, 11):
        medques[i].extend(tempdata[k:k + 4])
        k = k + 4

    hardques = {
        1: ['https://leetcode.com/problems/text-justification/', 'Text Justification'],
        2: ['https://leetcode.com/problems/integer-to-english-words/', 'Integer To English Words'],
        3: ['https://leetcode.com/problems/minimum-window-substring/', 'Minimum Window Substring'],
        4: ['https://leetcode.com/problems/valid-number/', 'Valid Number'],
        5: ['https://leetcode.com/problems/distinct-subsequences/', 'Distinct Subsequences'],
        6: ['https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/',
            'Smallest Range Covering Elements From K Lists'],
        7: ['https://leetcode.com/problems/substring-with-concatenation-of-all-words/',
            'Substring With Concatenation Of All Words']
    }
    for i in range(1, 8):
        hardques[i].extend(tempdata[k:k + 4])
        k = k + 4

    context = {
        'easyques': easyques,
        'medques': medques,
        'hardques': hardques,
    }
    return render(request, 'sheet/Strings.html', context)


def rec(request):
    if request.POST:
        data = recursion.Recur.objects.get(uid=request.user)
        for i in request.POST.keys():
            if i == 'csrfmiddlewaretoken':
                continue
            setattr(data, i, request.POST[i])
        data.save()
    data = recursion.Recur.objects.get(uid=request.user)
    tempdata = list(RecurForm(instance=data))
    k = 1

    # Recursion
    rques = {
        1: ['https://leetcode.com/problems/powx-n/', 'Powx N'],
        2: ['https://leetcode.com/problems/valid-palindrome/', 'Valid Palindrome'],
        3: ['https://leetcode.com/problems/subsets/', 'Subsets'],
        4: ['https://leetcode.com/problems/permutations/', 'Permutations'],
        5: ['https://leetcode.com/problems/permutations-ii/', 'Permutations Ii'],
        6: ['https://leetcode.com/problems/subsets-ii/', 'Subsets Ii'],
        7: ['https://leetcode.com/problems/combinations/', 'Combinations'],
        8: ['https://leetcode.com/problems/combination-sum/', 'Combination Sum'],
        9: ['https://leetcode.com/problems/combination-sum-ii/', 'Combination Sum Ii'],
        10: ['https://leetcode.com/problems/combination-sum-iii/', 'Combination Sum Iii'],
        11: ['https://leetcode.com/problems/letter-combinations-of-a-phone-number/',
             'Letter Combinations Of A Phone Number'],
        12: ['https://leetcode.com/problems/partition-to-k-equal-sum-subsets/', 'Partition To K Equal Sum Subsets'],
        13: ['https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/',
             'Maximum Length Of A Concatenated String With Unique Characters'],
        14: ['https://leetcode.com/problems/flood-fill/', 'Flood Fill'],
        15: ['https://leetcode.com/problems/word-search/', 'Word Search']
    }
    for i in range(1, 16):
        rques[i].extend(tempdata[k:k + 4])
        k = k + 4

    # Backtracking
    bmedques = {
        1: ['https://leetcode.com/problems/palindrome-partitioning/', 'Palindrome Partitioning'],
        2: ['https://leetcode.com/problems/beautiful-arrangement/', 'Beautiful Arrangement']
    }
    for i in range(1, 3):
        bmedques[i].extend(tempdata[k:k + 4])
        k = k + 4

    bhardques = {
        1: ['https://leetcode.com/problems/word-search-ii/', 'Word Search Ii'],
        2: ['https://leetcode.com/problems/sudoku-solver/', 'Sudoku Solver'],
        3: ['https://leetcode.com/problems/n-queens/', 'N Queens'],
        4: ['https://leetcode.com/problems/unique-paths-iii/', 'Unique Paths Iii']
    }
    for i in range(1, 5):
        bhardques[i].extend(tempdata[k:k + 4])
        k = k + 4

    # Design
    dques = {
        1: ['https://leetcode.com/problems/lru-cache/', 'Lru Cache'],
        2: ['https://leetcode.com/problems/find-median-from-data-stream/', 'Find Median From Data Stream'],
        3: ['https://leetcode.com/problems/design-underground-system/', 'Design Underground System'],
        4: ['https://leetcode.com/problems/lfu-cache/', 'Lfu Cache'],
        5: ['https://leetcode.com/problems/tweet-counts-per-frequency/', 'Tweet Counts Per Frequency'],
        6: ['https://leetcode.com/problems/all-oone-data-structure/', 'All Oone Data Structure'],
        7: ['https://leetcode.com/problems/design-browser-history/', 'Design Browser History']
    }
    for i in range(1, 8):
        dques[i].extend(tempdata[k:k + 4])
        k = k + 4

    context = {
        'rques': rques,
        'bmedques': bmedques,
        'bhardques': bhardques,
        'dques': dques,
    }
    return render(request, 'sheet/Recursion.html', context)


def llist(request):
    if request.POST:
        data = linklist.LinkedL.objects.get(uid=request.user)
        for i in request.POST.keys():
            if i == 'csrfmiddlewaretoken':
                continue
            setattr(data, i, request.POST[i])
        data.save()
    data = linklist.LinkedL.objects.get(uid=request.user)
    tempdata = list(LinkedForm(instance=data))
    k = 1

    easyques = {
        1: ['https://leetcode.com/problems/delete-node-in-a-linked-list/', 'Delete Node In A Linked List'],
        2: ['https://leetcode.com/problems/middle-of-the-linked-list/', 'Middle Of The Linked List'],
        3: ['https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/',
            'Convert Binary Number In A Linked List To Integer'],
        4: ['https://leetcode.com/problems/design-hashset/', 'Design Hashset'],
        5: ['https://leetcode.com/problems/design-hashmap/', 'Design Hashmap'],
        6: ['https://leetcode.com/problems/reverse-linked-list/', 'Reverse Linked List'],
        7: ['https://leetcode.com/problems/merge-two-sorted-lists/', 'Merge Two Sorted Lists'],
        8: ['https://leetcode.com/problems/remove-duplicates-from-sorted-list/', 'Remove Duplicates From Sorted List'],
        9: ['https://leetcode.com/problems/intersection-of-two-linked-lists/', 'Intersection Of Two Linked Lists'],
        10: ['https://leetcode.com/problems/linked-list-cycle/', 'Linked List Cycle'],
        11: ['https://leetcode.com/problems/palindrome-linked-list/', 'Palindrome Linked List'],
        12: ['https://leetcode.com/problems/remove-linked-list-elements/', 'Remove Linked List Elements']
    }
    for i in range(1, 13):
        easyques[i].extend(tempdata[k:k + 4])
        k = k + 4

    medques = {
        1: ['https://leetcode.com/problems/add-two-numbers/', 'Add Two Numbers'],
        2: ['https://leetcode.com/problems/copy-list-with-random-pointer/', 'Copy List With Random Pointer'],
        3: ['https://leetcode.com/problems/add-two-numbers-ii/', 'Add Two Numbers Ii'],
        4: ['https://leetcode.com/problems/reverse-linked-list-ii/', 'Reverse Linked List Ii'],
        5: ['https://leetcode.com/problems/reorder-list/', 'Reorder List'],
        6: ['https://leetcode.com/problems/remove-nth-node-from-end-of-list/', 'Remove Nth Node From End Of List'],
        7: ['https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/',
            'Flatten A Multilevel Doubly Linked List'],
        8: ['https://leetcode.com/problems/partition-list/', 'Partition List'],
        9: ['https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/',
            'Remove Duplicates From Sorted List Ii'],
        10: ['https://leetcode.com/problems/odd-even-linked-list/', 'Odd Even Linked List'],
        11: ['https://leetcode.com/problems/sort-list/', 'Sort List'],
        12: ['https://leetcode.com/problems/swap-nodes-in-pairs/', 'Swap Nodes In Pairs'],
        13: ['https://leetcode.com/problems/rotate-list/', 'Rotate List']
    }
    for i in range(1, 14):
        medques[i].extend(tempdata[k:k + 4])
        k = k + 4

    hardques = {
        1: ['https://leetcode.com/problems/merge-k-sorted-lists/', 'Merge K Sorted Lists'],
        2: ['https://leetcode.com/problems/reverse-nodes-in-k-group/', 'Reverse Nodes In K Group']
    }
    for i in range(1, 3):
        hardques[i].extend(tempdata[k:k + 4])
        k = k + 4

    context = {
        'easyques': easyques,
        'medques': medques,
        'hardques': hardques,
    }
    return render(request, 'sheet/Linked.html', context)


def tree(request):
    if request.POST:
        data = trees.Tree.objects.get(uid=request.user)
        for i in request.POST.keys():
            if i == 'csrfmiddlewaretoken':
                continue
            setattr(data, i, request.POST[i])
        data.save()
    data = trees.Tree.objects.get(uid=request.user)
    tempdata = list(TreeForm(instance=data))
    k = 1

    easyques = {
        1: ['https://leetcode.com/problems/diameter-of-binary-tree/', 'Diameter Of Binary Tree'],
        2: ['https://leetcode.com/problems/invert-binary-tree/', 'Invert Binary Tree'],
        3: ['https://leetcode.com/problems/subtree-of-another-tree/', 'Subtree Of Another Tree'],
        4: ['https://leetcode.com/problems/range-sum-of-bst/', 'Range Sum Of Bst'],
        5: ['https://leetcode.com/problems/symmetric-tree/', 'Symmetric Tree'],
        6: ['https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/',
            'Convert Sorted Array To Binary Search Tree'],
        7: ['https://leetcode.com/problems/merge-two-binary-trees/', 'Merge Two Binary Trees'],
        8: ['https://leetcode.com/problems/maximum-depth-of-binary-tree/', 'Maximum Depth Of Binary Tree'],
        9: ['https://leetcode.com/problems/binary-tree-paths/', 'Binary Tree Paths'],
        10: ['https://leetcode.com/problems/same-tree/', 'Same Tree'],
        11: ['https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/',
             'Lowest Common Ancestor Of A Binary Search Tree'],
        12: ['https://leetcode.com/problems/path-sum/', 'Path Sum'],
        13: ['https://leetcode.com/problems/minimum-absolute-difference-in-bst/', 'Minimum Absolute Difference In Bst'],
        14: ['https://leetcode.com/problems/sum-of-left-leaves/', 'Sum Of Left Leaves'],
        15: ['https://leetcode.com/problems/balanced-binary-tree/', 'Balanced Binary Tree'],
        16: ['https://leetcode.com/problems/binary-tree-inorder-traversal/', 'Binary Tree Inorder Traversal']
    }
    for i in range(1, 17):
        easyques[i].extend(tempdata[k:k + 4])
        k = k + 4

    medques = {
        1: ['https://leetcode.com/problems/count-good-nodes-in-binary-tree/', 'Count Good Nodes In Binary Tree'],
        2: ['https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/',
            'Lowest Common Ancestor Of A Binary Tree'],
        3: ['https://leetcode.com/problems/binary-tree-right-side-view/', 'Binary Tree Right Side View'],
        4: ['https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/',
            'All Nodes Distance K In Binary Tree'],
        5: ['https://leetcode.com/problems/validate-binary-search-tree/', 'Validate Binary Search Tree'],
        6: ['https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/',
            'Binary Tree Zigzag Level Order Traversal'],
        7: ['https://leetcode.com/problems/binary-search-tree-iterator/', 'Binary Search Tree Iterator'],
        8: ['https://leetcode.com/problems/binary-tree-level-order-traversal/', 'Binary Tree Level Order Traversal'],
        9: ['https://leetcode.com/problems/path-sum-iii/', 'Path Sum Iii'],
        10: ['https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/',
             'Construct Binary Tree From Preorder And Postorder Traversal'],
        11: ['https://leetcode.com/problems/unique-binary-search-trees/', 'Unique Binary Search Trees'],
        12: ['https://leetcode.com/problems/recover-binary-search-tree/', 'Recover Binary Search Tree'],
        13: ['https://leetcode.com/problems/populating-next-right-pointers-in-each-node/',
             'Populating Next Right Pointers In Each Node'],
        14: ['https://leetcode.com/problems/flatten-binary-tree-to-linked-list/', 'Flatten Binary Tree To Linked List'],
        15: ['https://leetcode.com/problems/maximum-width-of-binary-tree/', 'Maximum Width Of Binary Tree'],
        16: ['https://leetcode.com/problems/unique-binary-search-trees-ii/', 'Unique Binary Search Trees Ii'],
        17: ['https://leetcode.com/problems/kth-smallest-element-in-a-bst/', 'Kth Smallest Element In A Bst'],
        18: ['https://leetcode.com/problems/redundant-connection/', 'Redundant Connection']
    }
    for i in range(1, 19):
        medques[i].extend(tempdata[k:k + 4])
        k = k + 4

    hardques = {
        1: ['https://leetcode.com/problems/serialize-and-deserialize-binary-tree/',
            'Serialize And Deserialize Binary Tree'],
        2: ['https://leetcode.com/problems/binary-tree-maximum-path-sum/', 'Binary Tree Maximum Path Sum'],
        3: ['https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/',
            'Vertical Order Traversal Of A Binary Tree'],
        4: ['https://leetcode.com/problems/binary-tree-cameras/', 'Binary Tree Cameras'],
        5: ['https://leetcode.com/problems/sum-of-distances-in-tree/', 'Sum Of Distances In Tree'],
        6: ['https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/',
            'Number Of Ways To Reconstruct A Tree'],
        7: ['https://leetcode.com/problems/redundant-connection-ii/', 'Redundant Connection Ii']
    }
    for i in range(1, 8):
        hardques[i].extend(tempdata[k:k + 4])
        k = k + 4

    context = {
        'easyques': easyques,
        'medques': medques,
        'hardques': hardques,
    }
    return render(request, 'sheet/Tree.html', context)


def heap(request):
    if request.POST:
        data = heaps.Heap.objects.get(uid=request.user)
        for i in request.POST.keys():
            if i == 'csrfmiddlewaretoken':
                continue
            setattr(data, i, request.POST[i])
        data.save()
    data = heaps.Heap.objects.get(uid=request.user)
    tempdata = list(HeapForm(instance=data))
    k = 1

    medques = {
        1: ['https://leetcode.com/problems/k-closest-points-to-origin/', 'K Closest Points To Origin'],
        2: ['https://leetcode.com/problems/kth-largest-element-in-an-array/', 'Kth Largest Element In An Array'],
        3: ['https://leetcode.com/problems/reorganize-string/', 'Reorganize String'],
        4: ['https://leetcode.com/problems/furthest-building-you-can-reach/', 'Furthest Building You Can Reach'],
        5: ['https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/',
            'Kth Smallest Element In A Sorted Matrix'],
        6: ['https://leetcode.com/problems/cheapest-flights-within-k-stops/', 'Cheapest Flights Within K Stops'],
        7: ['https://leetcode.com/problems/find-the-most-competitive-subsequence/',
            'Find The Most Competitive Subsequence'],
        8: ['https://leetcode.com/problems/ugly-number-ii/', 'Ugly Number Ii']
    }
    for i in range(1, 9):
        medques[i].extend(tempdata[k:k + 4])
        k = k + 4

    hardques = {
        1: ['https://leetcode.com/problems/merge-k-sorted-lists/', 'Merge K Sorted Lists'],
        2: ['https://leetcode.com/problems/sliding-window-maximum/', 'Sliding Window Maximum'],
        3: ['https://leetcode.com/problems/the-skyline-problem/', 'The Skyline Problem'],
        4: ['https://leetcode.com/problems/trapping-rain-water-ii/', 'Trapping Rain Water Ii'],
        5: ['https://leetcode.com/problems/minimum-number-of-refueling-stops/', 'Minimum Number Of Refueling Stops'],
        6: ['https://leetcode.com/problems/swim-in-rising-water/', 'Swim In Rising Water'],
        7: ['https://leetcode.com/problems/shortest-path-to-get-all-keys/', 'Shortest Path To Get All Keys'],
        8: ['https://leetcode.com/problems/minimum-cost-to-hire-k-workers/', 'Minimum Cost To Hire K Workers'],
        9: ['https://leetcode.com/problems/k-th-smallest-prime-fraction/', 'K Th Smallest Prime Fraction']
    }
    for i in range(1, 10):
        hardques[i].extend(tempdata[k:k + 4])
        k = k + 4

    context = {
        'medques': medques,
        'hardques': hardques,
    }
    return render(request, 'sheet/Heap.html', context)


def trav(request):
    if request.POST:
        data = traversal.Trav.objects.get(uid=request.user)
        for i in request.POST.keys():
            if i == 'csrfmiddlewaretoken':
                continue
            setattr(data, i, request.POST[i])
        data.save()
    data = traversal.Trav.objects.get(uid=request.user)
    tempdata = list(TravForm(instance=data))
    k = 1

    # Breadth First Search
    bmedques = {
        1: ['https://leetcode.com/problems/number-of-islands/', 'Number Of Islands'],
        2: ['https://leetcode.com/problems/rotting-oranges/', 'Rotting Oranges'],
        3: ['https://leetcode.com/problems/snakes-and-ladders/', 'Snakes And Ladders'],
        4: ['https://leetcode.com/problems/is-graph-bipartite/', 'Is Graph Bipartite'],
        5: ['https://leetcode.com/problems/minimum-jumps-to-reach-home/', 'Minimum Jumps To Reach Home']
    }
    for i in range(1, 6):
        bmedques[i].extend(tempdata[k:k + 4])
        k = k + 4

    bhardques = {
        1: ['https://leetcode.com/problems/word-ladder/', 'Word Ladder'],
        2: ['https://leetcode.com/problems/word-ladder-ii/', 'Word Ladder Ii'],
        3: ['https://leetcode.com/problems/cut-off-trees-for-golf-event/', 'Cut Off Trees For Golf Event'],
        4: ['https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/', 'Reachable Nodes In Subdivided Graph']
    }
    for i in range(1, 5):
        bhardques[i].extend(tempdata[k:k + 4])
        k = k + 4

    # Depth First Search
    dmedques = {
        1: ['https://leetcode.com/problems/letter-combinations-of-a-phone-number/',
            'Letter Combinations Of A Phone Number'],
        2: ['https://leetcode.com/problems/course-schedule-ii/', 'Course Schedule Ii'],
        3: ['https://leetcode.com/problems/decode-string/', 'Decode String'],
        4: ['https://leetcode.com/problems/number-of-provinces/', 'Number Of Provinces'],
        5: ['https://leetcode.com/problems/clone-graph/', 'Clone Graph'],
        6: ['https://leetcode.com/problems/shortest-bridge/', 'Shortest Bridge'],
        7: ['https://leetcode.com/problems/all-paths-from-source-to-target/', 'All Paths From Source To Target'],
        8: ['https://leetcode.com/problems/surrounded-regions/', 'Surrounded Regions'],
        9: ['https://leetcode.com/problems/house-robber-iii/', 'House Robber Iii']
    }
    for i in range(1, 10):
        dmedques[i].extend(tempdata[k:k + 4])
        k = k + 4

    dhardques = {
        1: ['https://leetcode.com/problems/critical-connections-in-a-network/', 'Critical Connections In A Network'],
        2: ['https://leetcode.com/problems/remove-invalid-parentheses/', 'Remove Invalid Parentheses'],
        3: ['https://leetcode.com/problems/longest-increasing-path-in-a-matrix/',
            'Longest Increasing Path In A Matrix'],
        4: ['https://leetcode.com/problems/concatenated-words/', 'Concatenated Words'],
        5: ['https://leetcode.com/problems/making-a-large-island/', 'Making A Large Island'],
        6: ['https://leetcode.com/problems/contain-virus/', 'Contain Virus'],
        7: ['https://leetcode.com/problems/24-game/', '24 Game'],
        8: ['https://leetcode.com/problems/remove-boxes/', 'Remove Boxes']
    }
    for i in range(1, 4):
        dhardques[i].extend(tempdata[k:k + 4])
        k = k + 4

    context = {
        'bmedques': bmedques,
        'bhardques': bhardques,
        'dmedques': dmedques,
        'dhardques': dhardques,
    }
    return render(request, 'sheet/Trav.html', context)


def graph(request):
    if request.POST:
        data = graphs.Graph.objects.get(uid=request.user)
        for i in request.POST.keys():
            if i == 'csrfmiddlewaretoken':
                continue
            setattr(data, i, request.POST[i])
        data.save()
    data = graphs.Graph.objects.get(uid=request.user)
    tempdata = list(GraphForm(instance=data))
    k = 1

    easyques = {
        1: ['https://leetcode.com/problems/employee-importance/', 'Employee Importance'],
        2: ['https://leetcode.com/problems/find-the-town-judge/', 'Find The Town Judge']
    }
    for i in range(1, 3):
        easyques[i].extend(tempdata[k:k + 4])
        k = k + 4

    medques = {
        1: ['https://leetcode.com/problems/evaluate-division/', 'Evaluate Division'],
        2: ['https://leetcode.com/problems/accounts-merge/', 'Accounts Merge'],
        3: ['https://leetcode.com/problems/network-delay-time/', 'Network Delay Time'],
        4: ['https://leetcode.com/problems/find-eventual-safe-states/', 'Find Eventual Safe States'],
        5: ['https://leetcode.com/problems/keys-and-rooms/', 'Keys And Rooms'],
        6: ['https://leetcode.com/problems/possible-bipartition/', 'Possible Bipartition'],
        7: ['https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/',
            'Most Stones Removed With Same Row Or Column'],
        8: ['https://leetcode.com/problems/regions-cut-by-slashes/', 'Regions Cut By Slashes'],
        9: ['https://leetcode.com/problems/satisfiability-of-equality-equations/',
            'Satisfiability Of Equality Equations'],
        10: ['https://leetcode.com/problems/as-far-from-land-as-possible/', 'As Far From Land As Possible'],
        11: ['https://leetcode.com/problems/number-of-closed-islands/', 'Number Of Closed Islands'],
        12: ['https://leetcode.com/problems/number-of-operations-to-make-network-connected/',
             'Number Of Operations To Make Network Connected'], 13: [
            'https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/',
            'Find The City With The Smallest Number Of Neighbors At A Threshold Distance'],
        14: ['https://leetcode.com/problems/time-needed-to-inform-all-employees/',
             'Time Needed To Inform All Employees']
    }
    for i in range(1, 15):
        medques[i].extend(tempdata[k:k + 4])
        k = k + 4

    context = {
        'easyques': easyques,
        'medques': medques,
    }
    return render(request, 'sheet/Graph.html', context)


def dp(request):
    if request.POST:
        data = dynamic.DynamicP.objects.get(uid=request.user)
        for i in request.POST.keys():
            if i == 'csrfmiddlewaretoken':
                continue
            setattr(data, i, request.POST[i])
        data.save()
    data = dynamic.DynamicP.objects.get(uid=request.user)
    tempdata = list(DynamicForm(instance=data))
    k = 1

    easyques = {
        1: ['https://leetcode.com/problems/maximum-subarray/', 'Maximum Subarray'],
        2: ['https://leetcode.com/problems/climbing-stairs', 'Problems'],
        3: ['https://leetcode.com/problems/divisor-game/', 'Divisor Game'],
        4: ['https://leetcode.com/problems/counting-bits/', 'Counting Bits']
    }
    for i in range(1, 5):
        easyques[i].extend(tempdata[k:k + 4])
        k = k + 4

    medques = {
        1: ['https://leetcode.com/problems/decode-ways/', 'Decode Ways'],
        2: ['https://leetcode.com/problems/word-break/', 'Word Break'],
        3: ['https://leetcode.com/problems/delete-and-earn/', 'Delete And Earn'],
        4: ['https://leetcode.com/problems/maximal-square/', 'Maximal Square'],
        5: ['https://leetcode.com/problems/coin-change/', 'Coin Change'],
        6: ['https://leetcode.com/problems/maximum-product-subarray/', 'Maximum Product Subarray'],
        7: ['https://leetcode.com/problems/maximum-length-of-repeated-subarray/',
            'Maximum Length Of Repeated Subarray'],
        8: ['https://leetcode.com/problems/palindromic-substrings/', 'Palindromic Substrings'],
        9: ['https://leetcode.com/problems/house-robber/', 'House Robber'],
        10: ['https://leetcode.com/problems/continuous-subarray-sum/', 'Continuous Subarray Sum'],
        11: ['https://leetcode.com/problems/knight-dialer/', 'Knight Dialer'],
        12: ['https://leetcode.com/problems/longest-increasing-subsequence/', 'Longest Increasing Subsequence'],
        13: ['https://leetcode.com/problems/unique-paths/', 'Unique Paths'],
        14: ['https://leetcode.com/problems/count-square-submatrices-with-all-ones/',
             'Count Square Submatrices With All Ones'],
        15: ['https://leetcode.com/problems/range-sum-query-2d-immutable/', 'Range Sum Query 2D Immutable'],
        16: ['https://leetcode.com/problems/longest-arithmetic-subsequence/', 'Longest Arithmetic Subsequence']
    }
    for i in range(1, 17):
        medques[i].extend(tempdata[k:k + 4])
        k = k + 4

    hardques = {
        1: ['https://leetcode.com/problems/trapping-rain-water/', 'Trapping Rain Water'],
        2: ['https://leetcode.com/problems/word-break-ii/', 'Word Break Ii'],
        3: ['https://leetcode.com/problems/regular-expression-matching/', 'Regular Expression Matching'],
        4: ['https://leetcode.com/problems/maximal-rectangle/', 'Maximal Rectangle'],
        5: ['https://leetcode.com/problems/longest-valid-parentheses/', 'Longest Valid Parentheses'],
        6: ['https://leetcode.com/problems/edit-distance/', 'Edit Distance'],
        7: ['https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/',
            'Minimum Difficulty Of A Job Schedule'], 8: ['https://leetcode.com/problems/frog-jump/', 'Frog Jump'],
        9: ['https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/', 'Best Time To Buy And Sell Stock Iv'],
        10: ['https://leetcode.com/problems/burst-balloons/', 'Burst Balloons'],
        11: ['https://leetcode.com/problems/minimum-cost-to-merge-stones/', 'Minimum Cost To Merge Stones'],
        12: ['https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/',
             'Minimum Insertion Steps To Make A String Palindrome'],
        13: ['https://leetcode.com/problems/super-egg-drop/', 'Super Egg Drop'],
        14: ['https://leetcode.com/problems/count-different-palindromic-subsequences/',
             'Count Different Palindromic Subsequences'],
        15: ['https://leetcode.com/problems/minimum-cost-to-cut-a-stick/', 'Minimum Cost To Cut A Stick']
    }
    for i in range(1, 16):
        hardques[i].extend(tempdata[k:k + 4])
        k = k + 4

    context = {
        'easyques': easyques,
        'medques': medques,
        'hardques': hardques,
    }
    return render(request, 'sheet/Dynamic.html', context)


def misc(request):
    if request.POST:
        data = miscs.Misc.objects.get(uid=request.user)
        for i in request.POST.keys():
            if i == 'csrfmiddlewaretoken':
                continue
            setattr(data, i, request.POST[i])
        data.save()
    data = miscs.Misc.objects.get(uid=request.user)
    tempdata = list(MiscForm(instance=data))
    k = 1

    # Bit Manipulation
    bitques = {
        1: [
            'https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently',
            'Bit Manipulation'],
    }
    for i in range(1, 2):
        bitques[i].extend(tempdata[k:k + 4])
        k = k + 4

    # Tries
    trieques = {
        1: ['https://leetcode.com/explore/learn/card/trie/', 'Trie']
    }
    for i in range(1, 2):
        trieques[i].extend(tempdata[k:k + 4])
        k = k + 4

    # Segment Tree
    segtques = {
        1: ['https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/',
            'A Recursive Approach To Segment Trees Range Sum Queries Lazy Propagation']
    }
    for i in range(1, 2):
        segtques[i].extend(tempdata[k:k + 4])
        k = k + 4

    context = {
        'bitques': bitques,
        'trieques': trieques,
        'segtques': segtques,
    }
    return render(request, 'sheet/Misc.html', context)
