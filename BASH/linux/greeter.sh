#!/bin/bash
echo "HELLO!"
sleep 0.5

# loading() {
#     local count=0
#     local max=3
#     local delay=1
#     while true; do
#         if [ $count -eq $max ]; then
#             count=0
#         else
#             count=$((count + 1))
#         fi

#         echo -n "Loading "
#         for ((i = 0; i < count; i++)); do
#             echo -n "."
#         done
#         sleep $delay
#         echo -ne "\r"
#     done
# }

loading() {
    echo -n "Loading "
    sleep 1
    echo -n "."
    sleep 1
    echo -n "."
    sleep 1
    echo "."
    sleep 0.5

}
loading
echo "What is your name?"
read name
sleep 1
echo "What chapter are you on in Linux Basics For Hackers?"
read chapter
sleep 2
echo "WELCOME TO LIMBO" $name "You are now on chapter" $chapter "of Linux Basics For Hackers!"
echo -n "Hit ENTER to continue..."
read ENTER
loading
echo "YOU'RE NOW BORNE AGAIN!!!"
