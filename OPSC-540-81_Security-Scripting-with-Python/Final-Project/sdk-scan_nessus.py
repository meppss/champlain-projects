'''
Michael Epstein
OPSC-540-81
'''
# import statements
from tenable_io.client import TenableIOClient
from tenable_io.api.scans import ScanCreateRequest
from tenable_io.api.models import ScanSettings

# code
client = TenableIOClient(access_key='{YOUR ACCESS KEY}', secret_key='{YOUR SECRET KEY}') # initializes client with API keys from Nessus
scanners = {scanner.name: scanner.id for scanner in client.scanners_api.list().scanners}
template = client.scan_helper.template(name='basic')
scan_id = client.scans_api.create(
 ScanCreateRequest(
 template.uuid,
 ScanSettings(
‘{Scripted Scan}’,
 ‘{target}’,
 scanner_id=scanners['{scanner.name}']
 )
 )
)
scan = client.scan_helper.id(scan_id)
scan.launch()