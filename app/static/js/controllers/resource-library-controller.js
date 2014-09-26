angular.module('plo')
  .controller('ResourceLibraryController', ['$scope', 'Resource', function ($scope, Resource) {
    $scope.all = function () {
      Resource.query().$promise.then(function (resources) {
        $scope.rows = [];

        while (resources.length) {
          $scope.rows.push(resources.splice(0, 2));
        }
      });
    };
  }]);
