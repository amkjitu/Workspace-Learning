<?php

class Calc
{
    private $num1;
    private $sign;
    private $num2;

    public function __construct($num1, $sign, $num2)
    {
        $this->num1 = $num1;
        $this->sign = $sign;
        $this->num2 = $num2;
    }

    public function Calculate()
    {
        switch ($this->sign) {
            case 'addition':
                $ans = $this->num1 + $this->num2;
                return $ans;
                break;
            case 'subtraction':
                $ans = $this->num1 - $this->num2;
                return $ans;
                break;
            case 'multiplication':
                $ans = $this->num1 * $this->num2;
                return $ans;
                break;
            case 'division':
                $ans = $this->num1 / $this->num2;
                return $ans;
                break;

            default:
                echo "error";
                break;
        }
    }
}
