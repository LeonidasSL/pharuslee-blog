export const languages = {
  ko: '한국어',
  en: 'English',
} as const;

export type Lang = keyof typeof languages;

export const defaultLang: Lang = 'ko';

export const ui = {
  ko: {
    'site.title': 'Pharus Lee',
    'site.description': '의식, 영성, 그리고 기술의 교차점에서 글을 쓰는 작가',
    'nav.home': '홈',
    'nav.about': '저자 소개',
    'nav.blog': '에세이',
    'nav.book': '책 소개',
    'blog.readMore': '계속 읽기',
    'blog.readingTime': '{n}분 읽기',
    'blog.allPosts': '모든 에세이',
    'blog.latestPosts': '최근 에세이',
    'blog.noPosts': '아직 게시된 글이 없습니다.',
    'book.title': '다가올 우주적 각성을 위한 영혼의 가이드북',
    'book.buyNow': '구매하기',
    'book.learnMore': '자세히 보기',
    'home.hero.tagline': '의식의 깊은 곳에서 길어올린 이야기',
    'home.about.more': '더 알아보기',
    'footer.copyright': 'Pharus Lee. All rights reserved.',
    'lang.switch': 'English',
  },
  en: {
    'site.title': 'Pharus Lee',
    'site.description': 'Writer exploring the intersection of consciousness, spirituality, and technology',
    'nav.home': 'Home',
    'nav.about': 'About',
    'nav.blog': 'Essays',
    'nav.book': 'The Book',
    'blog.readMore': 'Read more',
    'blog.readingTime': '{n} min read',
    'blog.allPosts': 'All Essays',
    'blog.latestPosts': 'Latest Essays',
    'blog.noPosts': 'No posts yet.',
    'book.title': "A Soul's Guidebook for the Coming Cosmic Awakening",
    'book.buyNow': 'Buy Now',
    'book.learnMore': 'Learn more',
    'home.hero.tagline': 'Stories drawn from the depths of consciousness',
    'home.about.more': 'Learn more',
    'footer.copyright': 'Pharus Lee. All rights reserved.',
    'lang.switch': '한국어',
  },
} as const;

export function useTranslations(lang: Lang) {
  return function t(key: keyof (typeof ui)['ko']): string {
    return ui[lang][key] || ui[defaultLang][key] || key;
  };
}

export function getLangFromUrl(url: URL): Lang {
  const [, lang] = url.pathname.split('/');
  if (lang in languages) return lang as Lang;
  return defaultLang;
}

export function getAlternateLang(lang: Lang): Lang {
  return lang === 'ko' ? 'en' : 'ko';
}
