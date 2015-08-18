var app = angular.module("app", [])

var controller = function($scope, $http, $log){
    $scope.current_dataset = [{
        name: "Soul of Zendikar",
        type: "Creature",
        rarity: "Uncommon",
        artist: "Vincent Proce",
        set: "Magic 2015" }]

    $scope.change_detected = function(){

        function build_url(){
            var remove_last_character = function(string_arg){
                return string_arg.slice(0, string_arg.length - 1)
            }

            // dictionary building step
            var arg_dict = {}
            if($scope.powerCheckbox && $scope.powerDropDown.length > 0){
                arg_dict["power"] = $scope.powerDropDown
            }

            if($scope.toughnessCheckbox && $scope.toughnessDropDown.length > 0){
                arg_dict["toughness"] = $scope.toughnessDropDown
            }

            if($scope.colorCheckbox && $scope.colorDropDown.length > 0){
                arg_dict["color"] = $scope.colorDropDown
            }

            if($scope.loyaltyCheckbox && $scope.loyaltyDropDown.length > 0){
                arg_dict["loyalty"] = $scope.loyaltyDropDown
            }

            // looping through the dictionary to build the url step
            var final_url = "/lookupcards?"

            for(var key in arg_dict){
                final_url += key + "=" + arg_dict[key] + "&"
            }

            final_url = remove_last_character(final_url)
            return final_url
        }

        var url = build_url()
        $http.get(url).success(function(results){
            $scope.current_dataset = results["results"]
        })
    }
}

app.controller("controller", controller)