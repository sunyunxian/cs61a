#!/usr/bin/env bash

function run_each_questions(){
    fn_arr=("a_plus_abs_b" "a_plus_abs_b_syntax_check" "two_of_three" "two_of_three_syntax_check")

    for fn in ${fn_arr[@]}
    do
        python ok -q ${fn} --local
    done
}

function run_all_local(){
    python3 ok --local
}

function get_score_local(){
    python ok --score --local
}
