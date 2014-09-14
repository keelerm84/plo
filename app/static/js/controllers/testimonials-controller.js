angular.module('plo')
  .controller('TestimonialsController', ['$scope', '$routeParams', 'Testimonial', function ($scope, $routeParams, Testimonial) {
    $scope.all = function () {
      $scope.testimonials = Testimonial.query();
    };

    $scope.find = function() {
      $scope.testimonial = Testimonial.get({ id: $routeParams.id });
    };
  }]);
