from odoo import models, api, fields
from pdf2image import convert_from_path
import base64
from io import BytesIO

class DocumentsDocument(models.Model):
    _inherit = 'documents.document'

