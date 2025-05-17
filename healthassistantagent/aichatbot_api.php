<?php

// User input from the front end
$user_input = trim($_GET['message'] ?? '');

$openaiApiKey = 'sk-proj--';

$_URL = "https://api.openai.com/v1/chat/completions";

$data = array(
		'model' => 'gpt-4o-mini',
		'instructions' => 'You are a customer support expert. You will receive questions about Health Services, booking appointments. Do your best to answer the questions',
		'name' => 'Health Services',
        'messages' => array('role' => 'user', 'content' => $user_input)
        
);

$options = array(
        'http' => array(
                'header'  => "Content-Type: application/json\r\nAuthorization: Bearer ".$openaiApiKey."\r\n",
                'method'  => 'POST',
                'content' => json_encode($data)
        ),
        "ssl"=>array("verify_peer"=>false, "verify_peer_name"=>false)
);

function getSslPage($url,$options,$openaiApiKey,$user_input) {
    $ch = curl_init();
    $headers = [
    'Content-Type: application/json',
    'Authorization: Bearer ".$openaiApiKey."',
    'Content-Type: application/json'
];


// Set up the request headers
$headers = [
    'Content-Type: application/json',
    'Authorization: ' . 'Bearer ' . $openaiApiKey,
];

// Set up the request body
$data = [
    'model' => 'gpt-4o-mini',  // Adjust the model if necessary
    'messages' => [
        ['role' => 'system', 'content' => 'You are a customer support expert. You will receive questions about Health Services, booking appointments. Do your best to answer the questions'],
        ['role' => 'user', 'content' => $user_input]
    ],
];

	curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
    curl_setopt($ch, CURLOPT_HEADER, false);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_REFERER, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
    
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');


    $result = curl_exec($ch);//print_r($result);
    curl_close($ch);
    return $result;
}

echo $result = getSslPage($_URL,$options,$openaiApiKey,$user_input);

?>

