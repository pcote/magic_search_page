var app = angular.module("app", [])

var controller = function($scope, $http, $log){
    $scope.current_dataset = [{
        name: "Soul of Zendikar",
        type: "Creature",
        rarity: "Uncommon",
        artist: "Vincent Proce",
        set: "Magic 2015" }]

    function build_url(){
        var remove_last_character = function(string_arg){
            return string_arg.slice(0, string_arg.length - 1)
        }

        // dictionary building step
        var arg_dict = {}
        if($scope.powerCheckbox && $scope.powerDropDown){
            arg_dict["power"] = $scope.powerDropDown
        }

        if($scope.toughnessCheckbox && $scope.toughnessDropDown){
            arg_dict["toughness"] = $scope.toughnessDropDown
        }

        if($scope.colorCheckbox && $scope.colorDropDown){
            arg_dict["color"] = $scope.colorDropDown
        }

        if($scope.loyaltyCheckbox && $scope.loyaltyDropDown){
            arg_dict["loyalty"] = $scope.loyaltyDropDown
        }

        if($scope.textCheckbox && $scope.textTextfield && $scope.textTextfield.search(/\S/) >= 0 ){
            arg_dict["text"] = escape($scope.textTextfield)
        }

        // looping through the dictionary to build the url step
        var final_url = "/lookupcards?"

        for(var key in arg_dict){
            final_url += key + "=" + arg_dict[key] + "&"
        }

        final_url = remove_last_character(final_url)
        return final_url
    }

    $scope.change_detected = function(){

        var server_update_needed = function(){
            if($scope.powerCheckbox && $scope.powerDropDown){
                return true
            }

            if($scope.toughnessCheckbox && $scope.toughnessDropDown){
                return true
            }

            if($scope.colorCheckbox && $scope.colorDropDown){
                return true
            }

            if($scope.loyaltyCheckbox && $scope.loyaltyDropDown){
                return true
            }

            return false
        }

        if(server_update_needed()){
            $log.info("server update needed")
            var url = build_url()
            $http.get(url).success(function(results){
                $scope.current_dataset = results["results"]
            })
        }
        else {
            $log.info("server update not needed right now")
            $scope.current_dataset = []
        }
    }

    $scope.text_change_detected = function(evt){
        var ENTER_KEY = 13
        if(evt.which == ENTER_KEY){
            if($scope.textTextfield && $scope.textTextfield.search(/\S/) >= 0){
                $log.info("server update needed")
                var url = build_url()
                $http.get(url).success(function(results){
                    $scope.current_dataset = results["results"]
                })
            }
        }
    }
}

app.controller("controller", controller)