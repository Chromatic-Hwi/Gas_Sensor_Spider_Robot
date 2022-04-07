#!/bin/bash -x

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

function check_sensor()
{
	d_m=50

	if [ $f_g1 -eq 0 ] && [ $f_g2 -eq 0 ] ; then
		f_m="$((RANDOM% 10))"
	elif [ $f_g1 -eq 0 ] && [ $f_g2 -eq 1 ] ; then
		f_m="$((RANDOM% 11+20))"
	elif [ $f_g1 -eq 1 ] && [ $f_g2 -eq 0 ] ; then
		f_m="$((RANDOM% 21+30))"
	elif [ $f_g1 -eq 1 ] && [ $f_g2 -eq 1 ] ; then
		f_m="$((RANDOM% 31+60))"
	else
		return 1
	fi

	if [ $l_g1 -eq 0 ] && [ $l_g2 -eq 0 ] ; then
		l_m="$((RANDOM% 10))"
	elif [ $l_g1 -eq 0 ] && [ $l_g2 -eq 1 ] ; then
		l_m="$((RANDOM% 11+20))"
	elif [ $l_g1 -eq 1 ] && [ $l_g2 -eq 0 ] ; then
		l_m="$((RANDOM% 21+30))"
	elif [ $l_g1 -eq 1 ] && [ $l_g2 -eq 1 ] ; then
		l_m="$((RANDOM% 31+60))"
	else
		return 1
	fi

	if [ $r_g1 -eq 0 ] && [ $r_g2 -eq 0 ] ; then
		r_m="$((RANDOM% 10))"
	elif [ $r_g1 -eq 0 ] && [ $r_g2 -eq 1 ] ; then
		r_m="$((RANDOM% 11+20))"
	elif [ $r_g1 -eq 1 ] && [ $r_g2 -eq 0 ] ; then
		r_m="$((RANDOM% 21+30))"
	elif [ $r_g1 -eq 1 ] && [ $r_g2 -eq 1 ] ; then
		r_m="$((RANDOM% 31+60))"
	else
		return 1
	fi

	if [ $b_g1 -eq 0 ] && [ $b_g2 -eq 0 ] ; then
		b_m="$((RANDOM% 10))"
	elif [ $b_g1 -eq 0 ] && [ $b_g2 -eq 1 ] ; then
		b_m="$((RANDOM% 11+20))"
	elif [ $b_g1 -eq 1 ] && [ $b_g2 -eq 0 ] ; then
		b_m="$((RANDOM% 21+30))"
	elif [ $b_g1 -eq 1 ] && [ $b_g2 -eq 1 ] ; then
		b_m="$((RANDOM% 31+60))"
	else
		return 1
	fi
}



function insert_db()
{

	echo "default : $d_m   front : $f_m   left : $l_m   right : $r_m   back : $b_m"

curl -X POST 'http://127.0.0.1:8086/write?db=gasdb&u=gasadmin&p=gasadmin' --data-binary "
 gasdb,host=spider default_m=$d_m
 gasdb,host=spider front_m=$f_m
 gasdb,host=spider left_m=$l_m
 gasdb,host=spider right_m=$r_m
 gasdb,host=spider back_m=$b_m"

}


while :
do

# gpio 를 이용한 센서값 읽기
f_g1=`gpio -g read 23`
f_g2=`gpio -g read 24`

l_g1=`gpio -g read 27`
l_g2=`gpio -g read 22`

r_g1=`gpio -g read 20`
r_g2=`gpio -g read 21`

b_g1=`gpio -g read 19`
b_g2=`gpio -g read 26`

check_sensor
insert_db
sleep 1

done

