'use strict';

angular.module('plo')
  .factory('Testimonial', ['$resource', function ($resource) {
    return $resource('plo/testimonials/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
