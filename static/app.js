var app = angular.module("app", [])

var controller = function($scope, $http, $log){
    $scope.current_dataset = [{
        name: "Soul of Zendikar",
        type: "Creature",
        rarity: "Uncommon",
        artist: "Vincent Proce",
        set: "Magic 2015" }]

    $scope.change_detected = function(){
    }
}

app.controller("controller", controller)