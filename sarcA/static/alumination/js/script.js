"use strict";

var $ = function $(sel, ctx) {
  return (ctx || document).querySelector(sel);
},
    on = function on(el, ev, fn) {
  return el.addEventListener(ev, fn);
};

var trigger = $('.trigger input'),
    html = $('html');
on(trigger, 'change', function (e) {
  return trigger.checked ? html.classList.add('menu-opened') : html.classList.remove('menu-opened');
});