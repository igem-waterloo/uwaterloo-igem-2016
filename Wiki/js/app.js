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

.controller('team', function team($scope){
  $scope.team = [
      {
        name: "Cody Receno",
        subteam: "Lab and Design",
        program: "2B Biology",
        bio: "Hello, thanks for clicking on me. As a reward I'd like to drop some knowledge. Did you know that octopuses (octopi/octopode okay?) lose an arm in order to give birth then die shortly after? Talk about commitment right? I get really excited about synthetic biology because it makes biology so much more intersting in that the possibilities are endless and can make anything happen! Harnessing the power of life in order to create the best 3D printer the universe has to offer. If you ever meet me, ask me if I'm a tree.",
        image: "",
        lead: false,
        reveal: false,
      },
           {
        name: "Cody Receno",
        subteam: "Lab and Design",
        program: "2B Biology",
        bio: "Hello, thanks for clicking on me. As a reward I'd like to drop some knowledge. Did you know that octopuses (octopi/octopode okay?) lose an arm in order to give birth then die shortly after? Talk about commitment right? I get really excited about synthetic biology because it makes biology so much more intersting in that the possibilities are endless and can make anything happen! Harnessing the power of life in order to create the best 3D printer the universe has to offer. If you ever meet me, ask me if I'm a tree.",
        image: "",
        lead: false,
        reveal: false,
      },
      {
        name: "Cody Receno",
        subteam: "Lab and Design",
        program: "2B Biology",
        bio: "Hello, thanks for clicking on me. As a reward I'd like to drop some knowledge. Did you know that octopuses (octopi/octopode okay?) lose an arm in order to give birth then die shortly after? Talk about commitment right? I get really excited about synthetic biology because it makes biology so much more intersting in that the possibilities are endless and can make anything happen! Harnessing the power of life in order to create the best 3D printer the universe has to offer. If you ever meet me, ask me if I'm a tree.",
        image: "",
        lead: false,
        reveal: false,
      },
      {
        name: "Cody Receno",
        subteam: "Lab and Design",
        program: "2B Biology",
        bio: "Hello, thanks for clicking on me. As a reward I'd like to drop some knowledge. Did you know that octopuses (octopi/octopode okay?) lose an arm in order to give birth then die shortly after? Talk about commitment right? I get really excited about synthetic biology because it makes biology so much more intersting in that the possibilities are endless and can make anything happen! Harnessing the power of life in order to create the best 3D printer the universe has to offer. If you ever meet me, ask me if I'm a tree.",
        image: "",
        lead: false,
        reveal: false,
      },
      {
        name: "Cody Receno",
        subteam: "Lab and Design",
        program: "2B Biology",
        bio: "Hello, thanks for clicking on me. As a reward I'd like to drop some knowledge. Did you know that octopuses (octopi/octopode okay?) lose an arm in order to give birth then die shortly after? Talk about commitment right? I get really excited about synthetic biology because it makes biology so much more intersting in that the possibilities are endless and can make anything happen! Harnessing the power of life in order to create the best 3D printer the universe has to offer. If you ever meet me, ask me if I'm a tree.",
        image: "",
        lead: false,
        reveal: false,
      },
      {
        name: "Cody Receno",
        subteam: "Lab and Design",
        program: "2B Biology",
        bio: "Hello, thanks for clicking on me. As a reward I'd like to drop some knowledge. Did you know that octopuses (octopi/octopode okay?) lose an arm in order to give birth then die shortly after? Talk about commitment right? I get really excited about synthetic biology because it makes biology so much more intersting in that the possibilities are endless and can make anything happen! Harnessing the power of life in order to create the best 3D printer the universe has to offer. If you ever meet me, ask me if I'm a tree.",
        image: "",
        lead: false,
        reveal: false,
      },
      {
        name: "Cody Receno",
        subteam: "Lab and Design",
        program: "2B Biology",
        bio: "Hello, thanks for clicking on me. As a reward I'd like to drop some knowledge. Did you know that octopuses (octopi/octopode okay?) lose an arm in order to give birth then die shortly after? Talk about commitment right? I get really excited about synthetic biology because it makes biology so much more intersting in that the possibilities are endless and can make anything happen! Harnessing the power of life in order to create the best 3D printer the universe has to offer. If you ever meet me, ask me if I'm a tree.",
        image: "",
        lead: false,
        reveal: false,
      },
      {
        name: "Cody Receno",
        subteam: "Lab and Design",
        program: "2B Biology",
        bio: "Hello, thanks for clicking on me. As a reward I'd like to drop some knowledge. Did you know that octopuses (octopi/octopode okay?) lose an arm in order to give birth then die shortly after? Talk about commitment right? I get really excited about synthetic biology because it makes biology so much more intersting in that the possibilities are endless and can make anything happen! Harnessing the power of life in order to create the best 3D printer the universe has to offer. If you ever meet me, ask me if I'm a tree.",
        image: "",
        lead: false,
        reveal: false,
      },
      {
        name: "Cody Receno",
        subteam: "Lab and Design",
        program: "2B Biology",
        bio: "Hello, thanks for clicking on me. As a reward I'd like to drop some knowledge. Did you know that octopuses (octopi/octopode okay?) lose an arm in order to give birth then die shortly after? Talk about commitment right? I get really excited about synthetic biology because it makes biology so much more intersting in that the possibilities are endless and can make anything happen! Harnessing the power of life in order to create the best 3D printer the universe has to offer. If you ever meet me, ask me if I'm a tree.",
        image: "",
        lead: false,
        reveal: false,
      },
      {
        name: "Cody Receno",
        subteam: "Lab and Design",
        program: "2B Biology",
        bio: "Hello, thanks for clicking on me. As a reward I'd like to drop some knowledge. Did you know that octopuses (octopi/octopode okay?) lose an arm in order to give birth then die shortly after? Talk about commitment right? I get really excited about synthetic biology because it makes biology so much more intersting in that the possibilities are endless and can make anything happen! Harnessing the power of life in order to create the best 3D printer the universe has to offer. If you ever meet me, ask me if I'm a tree.",
        image: "",
        lead: false,
        reveal: false,
      },
      {
        name: "Cody Receno",
        subteam: "Lab and Design",
        program: "2B Biology",
        bio: "Hello, thanks for clicking on me. As a reward I'd like to drop some knowledge. Did you know that octopuses (octopi/octopode okay?) lose an arm in order to give birth then die shortly after? Talk about commitment right? I get really excited about synthetic biology because it makes biology so much more intersting in that the possibilities are endless and can make anything happen! Harnessing the power of life in order to create the best 3D printer the universe has to offer. If you ever meet me, ask me if I'm a tree.",
        image: "",
        lead: false,
        reveal: false,
      },
      {
        name: "Cody Receno",
        subteam: "Lab and Design",
        program: "2B Biology",
        bio: "Hello, thanks for clicking on me. As a reward I'd like to drop some knowledge. Did you know that octopuses (octopi/octopode okay?) lose an arm in order to give birth then die shortly after? Talk about commitment right? I get really excited about synthetic biology because it makes biology so much more intersting in that the possibilities are endless and can make anything happen! Harnessing the power of life in order to create the best 3D printer the universe has to offer. If you ever meet me, ask me if I'm a tree.",
        image: "",
        lead: false,
        reveal: false,
      }
  ]
})