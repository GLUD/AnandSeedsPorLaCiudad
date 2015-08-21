<?php
// src/AppBundle/Controller/LuckyController.php

namespace

 AppBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Symfony\Component\HttpFoundation\Response;

// class LuckyController extends Controller
// {
    // /**
     // * @Route("/lucky/number")
     // */
    // public function numberAction()
    // {
        // $number = rand(0, 100);
// 
        // return new Response(
            // '<html><body>Lucky number: '.$number.'</body></html>'
        // );
    // }
	
class LuckyController extends Controller
{
    // ...

    /**
     * @Route("/api/lucky/number")
     */
    public function apiNumberAction()
    {
        $data = array(
            'lucky_number' => rand(0, 100),
        );

        return new Response(
            json_encode($data),
            200,
            array('Content-Type' => 'application/json')
        );
    }
	
	
}

