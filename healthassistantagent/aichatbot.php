<!DOCTYPE html>
<html>
	<script src="ajax/libs/angularjs/1.6.9/angular.min.js"></script>
	<link href="css/styles.css" rel="stylesheet" type="text/css" />

	<body>
		<center>
			<div ng-app="myApp" ng-controller="myCtrl">

 				<div class="container" ng-repeat="message in messages" ng-class="{'container': $index % 2 === 0, 'darker': $index % 2 !== 0}">
  					<img src="images/iq-open-ai.png" alt="Open AI Avatar">
  					<p>{{ message }}</p>
  					<span class="time-right">{{ now | date:'HH:mm' }}</span>
				</div>

				<div ng-hide="isHidden">
  					<img src="images/iq-open-ai.png" alt="Open AI Avatar"><br />
					<h1>What can I help with?</h1>
				</div>

    			<input type="text" ng-model="newMessage" placeholder="Please, ask any question relating to your health" />
    			<button ng-click="sendMessage()">Send</button>

			</div>
		</center>
	</body>
	
</html>
<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $http)
{
    $scope.isHidden = false;
  
  	$scope.messages = [];$scope.messages_ = [];
    $scope.newMessage = '';

    $scope.sendMessage = function()
    {
    	if ($scope.newMessage)
    	{
    		if(!$scope.isHidden){$scope.isHidden = !$scope.isHidden;}
    		
    		$scope.messages.push($scope.newMessage);$scope.now = new Date();
    
    		$http.get("aichatbot_api.php?message="+$scope.newMessage).then(function (response) 
    		{
      			$scope.messages.push(response.data.choices[0].message.content);
      			
      			}, function(error) {
        		console.error('Error fetching data:', error);
  			});
  
    		$scope.newMessage = '';
    	}
    };
    
});
</script>
