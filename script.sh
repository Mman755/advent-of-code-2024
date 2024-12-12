AOC="~/Dropbox/Documents/Study/personal-study/advent-of-code-2024"
AOC_COOKIE="$AOCS"

function run_command () {
    local command=$1
    local part=$2
    local script=""

    if [[ $part -eq 1 ]]; then
        script="part1.py"
    elif [[ $part -eq 2 ]]; then
        script="part2.py"
    else
        echo "Invalid param"
        return 1
    fi

    case $command in
        aos)
            echo -ne '\e[0;32mInput: '; python3 $script < input.txt; echo -ne '\e[0m'
            ;;
        aot)
            echo -ne '\e[0;34mExample: '; python3 $script < example.txt; echo -ne '\e[0m'
            ;;
        aoc)
            echo -ne '\e[0;34mExample: '; python3 $script < example.txt; echo -ne '\e[0m'; echo
            echo -ne '\e[0;32mInput: '; python3 $script < input.txt; echo -ne '\e[0m'
            ;;
        *)
            echo "Unknown command: $command"
            return 1
            ;;
    esac
}

alias aos="run_command aos"
alias aot="run_command aot"
alias aoc="run_command aoc"

function aoc-load () {
    if [ $1 ]
    then
        curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$1/day/$2/input > input.txt
    else
        curl --cookie "session=$AOC_COOKIE" "$(echo date +https://adventofcode.com/%Y/day/%d/input | sed 's/\/0/\//g')" > input.txt
    fi
}
