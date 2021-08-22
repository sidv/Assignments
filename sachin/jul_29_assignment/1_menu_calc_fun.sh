#i/bin/bash


sum () {

	a=$1
	b=$2
	echo $((a+b))

}

mul () {

	a=$1
	b=$2
	echo $((a*b))
}

div () {
	a=$1
	b=$2
	echo $((a/b))
}


sub () {
	a=$1
	b=$2
	echo $((a-b))
}


while true
do
	echo "Press 1 for Addition"
	echo "Press 2 for Subtraction"
	echo "Press 3 for Division"
	echo "Press 4 for Multiplication"
	read choice
	echo "Enter First Number"
	read first
	echo "Enter Second Number"
	read second
	case $choice in
		1)
			result=$(sum $first $second)
			;;
		2)
			result=$(sub $first $second)
			;;
		3)
			result=$(div $first $second)
			;;
		4)
			result=$(mul $first $second)
			;;
		*)
			echo "Enter valid choice"
			;;
	esac



	echo $result" is result"

done
