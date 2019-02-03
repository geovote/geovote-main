const { NODE_ENV } = process.env
export const IS_DEBUG = true
export const IS_DEV = NODE_ENV === 'development'
export const IS_PROD = !IS_DEV

let calculatedLocalhost
if (typeof window !== 'undefined') {
  calculatedLocalhost =
    window.location.hostname === 'localhost' ||
    // [::1] is the IPv6 localhost address.
    window.location.hostname === '[::1]' ||
    // 127.0.0.1/8 is considered localhost for IPv4.
    window.location.hostname.match(
      /^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/
    )
}
export const IS_LOCALHOST = Boolean(calculatedLocalhost)

const CALC_ROOT_PATH = `${window.location.protocol}//${document.location.host}`
export const ROOT_PATH = CALC_ROOT_PATH || 'http://localhost:80/'
