EESchema Schematic File Version 4
LIBS:tetris-pcb-cache
EELAYER 26 0
EELAYER END
$Descr User 10984 8504
encoding utf-8
Sheet 1 1
Title "Proyecto Tetris"
Date "2019-06-28"
Rev ""
Comp "UMSS"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L power:GND #PWR0101
U 1 1 5D166547
P 4700 4600
F 0 "#PWR0101" H 4700 4350 50  0001 C CNN
F 1 "GND" H 4705 4427 50  0000 C CNN
F 2 "" H 4700 4600 50  0001 C CNN
F 3 "" H 4700 4600 50  0001 C CNN
	1    4700 4600
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0102
U 1 1 5D166599
P 3150 4300
F 0 "#PWR0102" H 3150 4150 50  0001 C CNN
F 1 "+5V" H 3165 4473 50  0000 C CNN
F 2 "" H 3150 4300 50  0001 C CNN
F 3 "" H 3150 4300 50  0001 C CNN
	1    3150 4300
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0103
U 1 1 5D1665EB
P 4300 4650
F 0 "#PWR0103" H 4300 4500 50  0001 C CNN
F 1 "+3.3V" H 4315 4823 50  0000 C CNN
F 2 "" H 4300 4650 50  0001 C CNN
F 3 "" H 4300 4650 50  0001 C CNN
	1    4300 4650
	1    0    0    -1  
$EndComp
Wire Wire Line
	3500 4350 3150 4350
Wire Wire Line
	3150 4350 3150 4300
$Comp
L nodemcu:NodeMCU_Amica_R2 U1
U 1 1 5D167134
P 3950 3650
F 0 "U1" H 3950 4575 50  0000 C CNN
F 1 "NodeMCU_Amica_R2" H 3950 4484 50  0000 C CNN
F 2 "NodeMCU:NodeMCU_Amica_R2" H 4200 3650 50  0001 C CNN
F 3 "" H 4200 3650 50  0000 C CNN
	1    3950 3650
	1    0    0    -1  
$EndComp
Wire Wire Line
	4400 4650 4300 4650
Wire Wire Line
	4400 4350 4400 4650
Wire Wire Line
	4400 4250 4700 4250
Wire Wire Line
	4700 4250 4700 4600
$Comp
L power:GND #PWR0104
U 1 1 5D166AF7
P 5350 4050
F 0 "#PWR0104" H 5350 3800 50  0001 C CNN
F 1 "GND" H 5355 3877 50  0000 C CNN
F 2 "" H 5350 4050 50  0001 C CNN
F 3 "" H 5350 4050 50  0001 C CNN
	1    5350 4050
	1    0    0    -1  
$EndComp
Text GLabel 4600 3850 2    50   Input ~ 0
Data
Text GLabel 4600 3650 2    50   Input ~ 0
Clock
Wire Wire Line
	4600 3650 4400 3650
Wire Wire Line
	4600 3850 4400 3850
$Comp
L power:+3.3V #PWR0105
U 1 1 5D1667A5
P 5350 3550
F 0 "#PWR0105" H 5350 3400 50  0001 C CNN
F 1 "+3.3V" H 5365 3723 50  0000 C CNN
F 2 "" H 5350 3550 50  0001 C CNN
F 3 "" H 5350 3550 50  0001 C CNN
	1    5350 3550
	1    0    0    -1  
$EndComp
Text GLabel 5850 3500 0    50   Input ~ 0
Clock
Text GLabel 5850 4000 0    50   Input ~ 0
Data
Wire Wire Line
	5850 4000 6150 4000
Wire Wire Line
	5850 3500 6150 3500
Wire Wire Line
	6150 3700 5350 3700
Wire Wire Line
	5350 3700 5350 3600
NoConn ~ 3500 3250
NoConn ~ 3500 3350
NoConn ~ 3500 3450
NoConn ~ 3500 3550
NoConn ~ 3500 3650
NoConn ~ 3500 3750
NoConn ~ 3500 3950
NoConn ~ 3500 4050
NoConn ~ 3500 4150
NoConn ~ 4400 4150
NoConn ~ 4400 4050
NoConn ~ 4400 3950
NoConn ~ 4400 3750
NoConn ~ 4400 3350
NoConn ~ 4400 3250
NoConn ~ 4400 3150
NoConn ~ 4400 3050
NoConn ~ 4400 2950
NoConn ~ 6150 3600
NoConn ~ 6150 3900
$Comp
L Connector_Generic:Conn_01x04 J3
U 1 1 5D16A842
P 7700 3000
F 0 "J3" V 7666 2712 50  0000 R CNN
F 1 "Conn_01x04" V 7575 2712 50  0000 R CNN
F 2 "Connector_Molex:Molex_KK-254_AE-6410-04A_1x04_P2.54mm_Vertical" H 7700 3000 50  0001 C CNN
F 3 "~" H 7700 3000 50  0001 C CNN
	1    7700 3000
	0    -1   -1   0   
$EndComp
$Comp
L power:+5V #PWR0106
U 1 1 5D16BB3B
P 7250 3200
F 0 "#PWR0106" H 7250 3050 50  0001 C CNN
F 1 "+5V" H 7265 3373 50  0000 C CNN
F 2 "" H 7250 3200 50  0001 C CNN
F 3 "" H 7250 3200 50  0001 C CNN
	1    7250 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	7600 3200 7600 3300
Wire Wire Line
	7600 3300 7250 3300
Wire Wire Line
	7250 3300 7250 3200
$Comp
L power:GND #PWR0107
U 1 1 5D16BCD3
P 7950 3900
F 0 "#PWR0107" H 7950 3650 50  0001 C CNN
F 1 "GND" H 7955 3727 50  0000 C CNN
F 2 "" H 7950 3900 50  0001 C CNN
F 3 "" H 7950 3900 50  0001 C CNN
	1    7950 3900
	1    0    0    -1  
$EndComp
Wire Wire Line
	7950 3850 7950 3900
Wire Wire Line
	7900 3850 7950 3850
Wire Wire Line
	7600 3700 7600 3300
Connection ~ 7600 3300
NoConn ~ 3500 2950
Wire Wire Line
	7800 4000 7800 3200
Wire Wire Line
	7700 3200 7700 3500
Wire Wire Line
	7700 3500 6950 3500
Wire Wire Line
	7900 3200 7900 3800
Wire Wire Line
	7800 4000 6950 4000
Wire Wire Line
	7600 3700 6950 3700
Wire Wire Line
	6950 3800 7900 3800
Connection ~ 7900 3800
Wire Wire Line
	7900 3800 7900 3850
NoConn ~ 6950 3600
NoConn ~ 6950 3900
$Comp
L digitalConverter:level-converter U2
U 1 1 5D16C923
P 6550 3550
F 0 "U2" H 6550 3825 50  0000 C CNN
F 1 "level-converter" H 6550 3734 50  0000 C CNN
F 2 "NodeMCU:level_converter" H 6550 2900 50  0001 C CNN
F 3 "" H 6550 2900 50  0001 C CNN
	1    6550 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	6150 3800 5350 3800
Wire Wire Line
	5350 3800 5350 4050
Wire Wire Line
	4400 3450 4700 3450
Wire Wire Line
	4700 3450 4700 3550
Wire Wire Line
	4700 3550 5200 3550
Wire Wire Line
	5200 3550 5200 3600
Wire Wire Line
	5200 3600 5350 3600
Connection ~ 5350 3600
Wire Wire Line
	5350 3600 5350 3550
$Comp
L power:GND #PWR0108
U 1 1 5D16D76C
P 2950 4050
F 0 "#PWR0108" H 2950 3800 50  0001 C CNN
F 1 "GND" H 2955 3877 50  0000 C CNN
F 2 "" H 2950 4050 50  0001 C CNN
F 3 "" H 2950 4050 50  0001 C CNN
	1    2950 4050
	1    0    0    -1  
$EndComp
Wire Wire Line
	3500 4250 3350 4250
Wire Wire Line
	3350 4250 3350 4000
Wire Wire Line
	3350 4000 2950 4000
Wire Wire Line
	2950 4000 2950 4050
Wire Wire Line
	3500 3850 3350 3850
Wire Wire Line
	3350 3850 3350 4000
Connection ~ 3350 4000
Wire Wire Line
	4400 3550 4550 3550
$Comp
L power:GND #PWR0109
U 1 1 5D16EC4B
P 4850 3250
F 0 "#PWR0109" H 4850 3000 50  0001 C CNN
F 1 "GND" H 4855 3077 50  0000 C CNN
F 2 "" H 4850 3250 50  0001 C CNN
F 3 "" H 4850 3250 50  0001 C CNN
	1    4850 3250
	-1   0    0    1   
$EndComp
Wire Wire Line
	4550 3550 4550 3400
Wire Wire Line
	4550 3400 4850 3400
Wire Wire Line
	4850 3400 4850 3250
$EndSCHEMATC