// Importing necessary modules and classes from Odoo's core and public widget library
import PublicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";
import { registry } from "@web/core/registry";

/**
 * DocumentWidget is a custom widget to display a list of documents on the webpage.
 * It fetches the list of documents using RPC calls to the Odoo backend and displays them
 * in a responsive card layout with information like the filename, thumbnail, and file type.
 */
export const DocumentWidget = PublicWidget.Widget.extend({
    
    // The selector specifies the HTML elements this widget will apply to
    selector: '.dynamic_snippet',

    /**
     * The start method is called when the widget is initialized.
     * It triggers the RPC call to fetch the list of documents and renders them on the page.
     * 
     * @async
     */
    async start() {
        try {
            // Making an asynchronous RPC call to fetch documents from the Odoo backend
            await rpc('/documents', {
                model: 'documents.document',  // Model to call the method on
                method: 'get_documents',      // The method to call on the model
                kwargs: {},                   // No keyword arguments are passed
                args: []                      // No positional arguments are passed
            }).then((result) => {
                // Handle the result after the RPC call is successful
                // Map through the result documents and create the HTML structure for each document
                const documentsList = result.documents.map((doc) => {
                    return `
                        <div class="col-md-3 document-card">
                            <div class="card">
                                <!-- Display the thumbnail image of the document -->
                                <img src="data:image/jpeg;base64,${doc.thumbnail}" class="card-img-top" alt="${doc.filename} Thumbnail"/>
                                <div class="card-body">
                                    <!-- Display the document filename as the title -->
                                    <h5 class="card-title">${doc.filename}</h5>
                                    <!-- Display the file type -->
                                    <p class="card-text">${doc.file_type}</p>
                                    <!-- Button to view the document -->
                                    <a href="${doc.file_url}" target="_blank" class="btn btn-primary">View Document</a>
                                </div>
                            </div>
                        </div>
                    `;
                }).join('');  // Join all document cards into a single HTML string

                // Inject the HTML for the documents into the '.documents' container in the DOM
                this.$('.documents').html(`<div class="row">${documentsList}</div>`);

            }).catch((error) => {
                // Handle any errors during the RPC call
                console.error("Error loading documents:", error);
            });
        } catch (error) {
            // Handle any unexpected errors during the widget's start method
            console.error("Unexpected error:", error);
        }
    },
});

// Register the DocumentWidget in the Odoo widget registry so it can be used in the frontend
PublicWidget.registry.document = DocumentWidget;

// Return the custom widget for use
return DocumentWidget;
