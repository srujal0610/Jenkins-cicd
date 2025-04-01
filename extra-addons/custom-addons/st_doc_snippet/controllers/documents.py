from odoo import http
from odoo.http import request


class Documents(http.Controller):
    """
    Controller for handling document-related operations, such as fetching documents
    and folder data from the 'documents.document' model. This is used for
    providing data for the frontend, especially for document and folder management.
    """

    @http.route(route='/documents', auth='public', csrf=False, type='json')
    def get_documents(self, **kwargs):
        """
        Fetches documents and folders from the 'documents.document' model.

        The function retrieves a list of folders (type='folder') and documents
        (type!='folder') and returns them as JSON to be consumed by the frontend.

        - Folders are listed as unique folder names.
        - Documents include details such as filename, file URL, file type, folder ID,
          and thumbnail.

        Returns:
            dict: A dictionary containing two keys:
                - 'documents': A list of dictionaries with document details.
                - 'folders': A list of unique folder names.
        """

        # Retrieve all folder records (type='folder') from the 'documents.document' model.
        folders = request.env['documents.document'].search([('type', '=', "folder")])

        folder_list = []
        # Loop through all folders and append their display name to the folder_list.
        for rec in folders:
            if rec.display_name:
                folder_list.append(rec.display_name)

        # Remove duplicates from folder_list to get unique folder names.
        unique_folders = list(set(folder_list))

        # Retrieve all document records that are not folders (type!='folder').
        documents = request.env['documents.document'].search([("type", "!=", "folder")])

        documents_data = []
        # Loop through each document and gather relevant details.
        for doc in documents:
            attachment = doc.attachment_id  # Fetch the associated attachment

            if attachment:
                # Retrieve the thumbnail associated with the document (if available).
                thumbnail_data = doc.thumbnail

                # Structure the document data to be returned in the response.
                file_data = {
                    'filename': attachment.name,  # Filename of the attachment
                    'file_url': '/web/content/%s' % attachment.id,  # URL to access the file
                    'file_type': attachment.mimetype,  # MIME type of the file
                    'folder_id': doc.folder_id.name,  # Name of the folder this document belongs to
                    'thumbnail': thumbnail_data  # Thumbnail associated with the document
                }

                # Append the file data dictionary to the documents_data list.
                documents_data.append(file_data)

        # Return the final data as a dictionary, containing documents and folders.
        return {
            'documents': documents_data,  # List of documents with their data
            'folders': unique_folders  # List of unique folder names
        }
