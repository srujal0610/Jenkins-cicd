//import options from "@web_editor/js/editor/snippets.options";
//import { rpc } from "@web/core/network/rpc";
//import { registry } from "@web/core/registry";
//
//options.registry.SnippetOptions = options.Class.extend({
//    start() {
//         rpc('/documents/',{
//            model: 'documents.document',
//            method: 'get_documents',
//            args: [],
//        }).then((result) => {
//            const selectOptEl = this.$('.categories');
//            for (const record of result.unique_folders) {
//                const buttonEl = document.createElement("we-option");
//                console.log(buttonEl)
//                buttonEl.textContent = record;
//                buttonEl.dataset.selectDataAttribute = record;
////                buttonEl.classList.add('categories');
////                return buttonEl
////                buttonEl.addEventListener('click', () => {
////                    console.log(`Button clicked: ${record}`);
////                });
//
//                selectOptEl.append(buttonEl);
//            }
//        }).catch((error) => {
//            console.error("Error fetching unique folders:", error);
//        });
//    },
//
//});


//import { rpc } from "@web/core/network/rpc";
//$(document).ready(function () {
//        // Event listener for category button click
//        $('.we-button').on('click', function () {
//            var category = $(this).text().trim();  // Get the name of the clicked button (category name)
//            fetchDocuments(category);  // Send RPC to fetch documents for that category
//        });
//
//        // Function to fetch documents based on category using RPC
//        function fetchDocuments(category) {
//            rpc.query({
//                model: 'documents.document',  // Model to query
//                method: 'get_documents_by_category',  // Method defined in Python controller
//                args: [category],  // Arguments passed to method (category name)
//            }).then(function (documents) {
//                displayDocuments(documents);  // Update the UI with fetched documents
//            }).catch(function () {
//                alert('Error fetching documents');
//            });
//        }
//
//        // Function to display the fetched documents
//        function displayDocuments(documents) {
//            var container = $('#documents-container');
//            container.empty();  // Clear any previously displayed documents
//
//            if (documents.length > 0) {
//                documents.forEach(function (doc) {
//                    var docElement = $('<div>').text(doc.name);  // Modify to show more info if needed
//                    container.append(docElement);
//                });
//            } else {
//                container.append('<p>No documents found for this category.</p>');
//            }
//        }
//    });

import  SnippetOptions  from "@web_editor/js/editor/snippets.options";
import { registry } from "@web/core/registry";
import { rpc } from "@web/core/network/rpc";


SnippetOptions.registry.document = SnippetOptions.Class.extend({
    selector: '.dynamic_snippet',

    start() {
        this._super(...arguments);
        this.$('.categories we-button').on('click', this.onCategoryClick.bind(this));
    },

    onCategoryClick(event) {
        const selectedCategory = $(event.target).data('category')
        console.log('Selected Category:', selectedCategory);
        this.fetchDocuments(selectedCategory);
    },


    async fetchDocuments(category) {
        console.log('Category passed to fetchDocuments:', category);
        this.$('.categories').val(category);

        await rpc('/documents', {
            model: 'documents.document',
            method: 'get_documents',
            args:[category]
        })
        .then((result) => {
            const documentsList = result.documents.map(doc => {
                return `<div><a href="${doc.file_url}" target="_blank">${doc.folder_id}&nbsp;${doc.filename}</a></div>`;
            }).join('');
            this.$('.documents').html(documentsList);
        })
        .catch((error) => {
            console.error("Error loading documents:", error);
        });
    },
});


registry.add('custom_category_options', SnippetOptions.registry.document);



//import SnippetOptions from "@web_editor/js/editor/snippets.options";
//import { registry } from "@web/core/registry";
//
//SnippetOptions.registry.document = SnippetOptions.Class.extend({
//    selector: '.dynamic_snippet',
//
//    start() {
//        this._super(...arguments);
//        this.$('.categories we-option').on('click', this.onCategoryClick.bind(this));
//    },
//
//    onCategoryClick(event) {
//        const selectedCategory = $(event.target).data('category');
//        console.log('Selected Category:', selectedCategory);
//        this.triggerPublicWidget(selectedCategory);
//    },
//
//    triggerPublicWidget(category) {
//        const documentWidget = registry.get('document');
//        if (documentWidget) {
//            documentWidget.updateDocuments(category); // Call method in PublicWidget
//        } else {
//            console.error("DocumentWidget not found in registry.");
//        }
//    },
//});
//
//registry.add('custom_category_options', SnippetOptions.registry.document);