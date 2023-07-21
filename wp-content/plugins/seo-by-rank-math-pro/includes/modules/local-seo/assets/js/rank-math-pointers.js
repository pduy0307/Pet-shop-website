(()=>{"use strict";var t={n:e=>{var n=e&&e.__esModule?()=>e.default:()=>e;return t.d(n,{a:n}),n},d:(e,n)=>{for(var o in n)t.o(n,o)&&!t.o(e,o)&&Object.defineProperty(e,o,{enumerable:!0,get:n[o]})},o:(t,e)=>Object.prototype.hasOwnProperty.call(t,e)};const e=jQuery;var n=t.n(e);const o=lodash,r=wp.i18n;function i(t,e){for(var n=0;n<e.length;n++){var o=e[n];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(t,o.key,o)}}var a=function(){function t(){!function(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}(this,t),this.pointers=this.getPointers(),this.showPointer=this.showPointer.bind(this),this.init()}var e,a,s;return e=t,(a=[{key:"init",value:function(){var t=this;(0,o.forEach)(this.pointers,(function(e,n){return t.showPointer(n),!1})),n()(".rank-math-toolbar-score").parent().hasClass("is-pressed")||n()(".rank-math-toolbar-score").parent().trigger("click")}},{key:"showPointer",value:function(t){var e=this,o=this.pointers[t],i=n().extend(o.options,{pointerClass:"wp-pointer rm-pointer",close:function(){o.next&&e.showPointer(o.next)},buttons:function(t,e){var o="wp-pointer-3"===e.pointer[0].id?(0,r.__)("Finish","rank-math-pro"):(0,r.__)("Next","rank-math-pro"),i=n()('<a class="close" href="#">'+(0,r.__)("Dismiss","rank-math-pro")+"</a>"),a=n()('<a class="button button-primary" href="#">'+o+"</a>"),s=n()('<div class="rm-pointer-buttons" />');return i.on("click.pointer",(function(t){t.preventDefault(),e.element.pointer("destroy")})),a.on("click.pointer",(function(t){t.preventDefault(),e.element.pointer("close")})),s.append(i),s.append(a),s}}),a=n()(o.target).pointer(i);a.pointer("open"),o.next_trigger&&n()(o.next_trigger.target).on(o.next_trigger.event,(function(){setTimeout((function(){a.pointer("close")}),400)}))}},{key:"getPointers",value:function(){return{title:{target:".editor-post-title__input",next:"schema",options:{content:"<h3>"+(0,r.__)("Local Business Name","rank-math-pro")+"</h3><p>"+(0,r.__)("Give your business's new location a name here. This field is required and will be visible to users.","rank-math-pro")+"</p>"}},schema:{target:".components-tab-panel__tabs-item.rank-math-schema-tab",next:"content",options:{content:"<h3>"+(0,r.__)("Local Business Schema","rank-math-pro")+"</h3><p>"+(0,r.__)('Add your local business\'s details here with "Local Business" Schema Markup in order to be eligible for local SERP features.',"rank-math-pro")+"</p>",position:{edge:"right",align:"left"}}},content:{target:".is-root-container",next:"submitdiv",options:{content:"<h3>"+(0,r.__)("Show Business Information","rank-math-pro")+"</h3><p>"+(0,r.sprintf)((0,r.__)("Make sure to add the Local Business Block or %s to display your business data.","rank-math-pro"),'<a href="https://rankmath.com/kb/location-data-shortcode/" target="_blank">[rank_math_local] shortcode</a>')+"</p>",position:{edge:"bottom",align:"middle"}}},submitdiv:{target:".editor-post-publish-button__button",next:"",options:{content:"<h3>"+(0,r.__)("Publish your location!","rank-math-pro")+"</h3><p>"+(0,r.__)("When you're done editing, don't forget to hit \"publish\" to create this location.","rank-math-pro")+"</p>"}}}}}])&&i(e.prototype,a),s&&i(e,s),Object.defineProperty(e,"prototype",{writable:!1}),t}();n()(window).on("load",(function(){new a}))})();