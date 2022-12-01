# first approach
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

# second approach
from ecommerce.shipping import calc_shipping
calc_shipping()

# third approach
from ecommerce import shipping
shipping.calc_shipping()