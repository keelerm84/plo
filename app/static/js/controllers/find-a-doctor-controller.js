angular.module('plo')
  .controller('FindDoctorController', ['$scope', function ($scope) {
    $scope.map = {
      center: {
        latitude: 0,
        longitude: 0
      },
      zoom: 2
    };
  }]);
