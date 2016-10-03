// Define the `waterloo` module
var waterloo = angular.module('waterloo', []);

// Define the `main` controller on the `waterloo` module
waterloo.controller('main', function main($scope) {
  $scope.host = "localhost:8000"
  $scope.things = [
    {
      name: 'Waterloo',
      snippet: 'Yaaaay Waterloo'
    }, {
      name: 'iGEM',
      snippet: 'iGEM is awesome too!'
    }, {
      name: 'Prions',
      snippet: 'Let\'s figure them out'
    }
  ];
})

.controller('protocols', function protocols($scope){
  $scope.active = ''
  $scope.testing = function(){
    console.log('testing')
  }
})