from register import register
from crawl import crawl
import check


# Parameters
L2_scope_acc_rev = "edi.yyy.2"
fname = "processing_log.csv"

# Processing log integrity checker
print("Processing log integrity checker")
check.add_level2(level2=L2_scope_acc_rev, filename=fname)
check.find_duplicates(filename=fname)
# TODO check package ID is in scope.accession.revision format

# Register the incoming L2_scope_acc_rev
gbif_id = register(level2=L2_scope_acc_rev, filename=fname)

# Launch crawler
crawl(level2=L2_scope_acc_rev, gbif_id=gbif_id)

# def main(L2_scope_acc_rev, fname):
#     L2_scope_acc_rev = "edi.yyy.2"
#     fname = "processing_log.csv"
#
#     # Processing log integrity checker
#     print("Processing log integrity checker")
#     check.add_level2(level2=L2_scope_acc_rev, filename=fname)
#     check.find_duplicates(filename=fname)
#     # TODO check package ID is in scope.accession.revision format
#
#     # Register the incoming L2_scope_acc_rev
#     gbif_id = register(level2=L2_scope_acc_rev, filename=fname)
#
#     # Launch crawler
#     crawl(level2=L2_scope_acc_rev, gbif_id=gbif_id)


