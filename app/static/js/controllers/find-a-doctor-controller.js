angular.module('plo')
  .controller('FindDoctorController', ['$scope', 'Doctor', function ($scope, Doctor) {

    $scope.all = function () {
      $scope.map = {
        center: {
          latitude: 0,
          longitude: 0
        },
        zoom: 2
      };

      $scope.doctors = Doctor.query();
    };
  }]);
