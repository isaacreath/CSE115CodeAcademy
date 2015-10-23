angular
  .module('MyApp')
  .controller('AppCtrl', function ($scope, $timeout, $mdSidenav, $log, $http) {
    $scope.toggleLeft = buildDelayedToggler('left');
    $scope.toggleRight = buildToggler('right');
    $scope.isOpenRight = function(){
      return $mdSidenav('right').isOpen();
    };

    $scope.submit = function(){
      var editor = ace.edit("editor");
      var code = editor.getValue();
      var codeJson = {"value": code};
      var config = {};
      /*
        This will work once Zach has an api up.
      */
      // $http.post("/url", JSON.stringify(codeJson), config).then(function(){
      //                                                             console.log("success");
      //                                                           }, 
      //                                                           function(){
      //                                                             console.log("error");
      //                                                           });
    }

    /**
     * Supplies a function that will continue to operate until the
     * time is up.
     */
    function debounce(func, wait, context) {
      var timer;

      return function debounced() {
        var context = $scope,
            args = Array.prototype.slice.call(arguments);
        $timeout.cancel(timer);
        timer = $timeout(function() {
          timer = undefined;
          func.apply(context, args);
        }, wait || 10);
      };
    }


    /**
     * Build handler to open/close a SideNav; when animation finishes
     * report completion in console
     */

     /*
        I'm not sure if I'm allowed to delete these but I'm too scare of what will happen to do that.
        - Isaac
     */
    function buildDelayedToggler(navID) {
      return debounce(function() {
        $mdSidenav(navID)
          .toggle()
          .then(function () {
            $log.debug("toggle " + navID + " is done");
          });
      }, 200);
    }

    function buildToggler(navID) {
      return function() {
        $mdSidenav(navID)
          .toggle()
          .then(function () {
            $log.debug("toggle " + navID + " is done");
          });
      }
    }
  })
  .controller('LeftCtrl', function ($scope, $timeout, $mdSidenav, $log) {
    $scope.close = function () {
      $mdSidenav('left').close()
        .then(function () {
          $log.debug("close LEFT is done");
        });

    };
  })
  .controller('RightCtrl', function ($scope, $timeout, $mdSidenav, $log) {
    $scope.close = function () {
      $mdSidenav('right').close()
        .then(function () {
          $log.debug("close RIGHT is done");
        });
    };
  });
