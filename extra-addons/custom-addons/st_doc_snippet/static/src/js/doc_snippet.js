import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";
import { registry } from "@web/core/registry";

publicWidget.registry.DocumentSnippet=publicWidget.Widget.extend({
    selector: '.dynamic_snippet',
     events: {
//            'mouseover #document_category option': '_onCategoryHover',
//            'click #document_category option': '_onCategoryClick',
              'focus .document_category':'_fetchCategories',
              'click .document_category':'_fetchCategories'
     },

     _initializeInteraction: function () {
        var self = this;

        // Listen for mouse click or focus event on the snippet or we-select dropdown
        var $snippet = document.querySelector('.dynamic_snippet');
        $snippet.addEventListener('click', function () {
            console.log("Click")
            self._fetchCategories();
        });
        $snippet.addEventListener('focus', function () {
            console.log("Focus")
            self._fetchCategories();
        });
    },

     start: function () {
            var self = this;

     },

     _fetchCategories: function(){
        var self=this;
        rpc('/documents',{
            model:'documents.document',
            method:'get_documents',
            args:[]
        }).then(function(res){
            console.log(res.folders)
            self._updateCategoryDropdown(res.folders);
        })
     },


      _updateCategoryDropdown: function(folders) {
        var self = this;
        var $dropdown = document.querySelector('.document_category');
        console.log($dropdown)
        if ($dropdown) {
            console.log('Dropdown element found:', $dropdown);

            $dropdown.innerHTML = '';

            folders.forEach(function(folder) {
                var option = document.createElement('');
                option.setAttribute('value', folder);
                option.textContent = folder;
                $dropdown.appendChild(option);
            });
        }
    }
})