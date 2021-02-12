import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    pages_links = corpus[page]
    model = {}
    if pages_links == []:
        for page in corpus:
            model[page] = 1 / len(corpus)
    else:
        for page in corpus:
            model[page] = (1-damping_factor)/len(corpus)
        for page in pages_links:
            model[page] += damping_factor/len(pages_links)

    return model


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    if n < 1:
        raise ValueError

    model = None
    pagerank = {}
    for i in range(0,n):
        if model == None:
            pages_number = len(corpus)
            pages_list = list(corpus.keys())
            first_choice = pages_list[random.randint(0, pages_number - 1)]
            model = transition_model(corpus, first_choice, damping_factor)
            for page in model:
                pagerank[page] = model[page]
        else:
            pages_list = list(model)
            probabilities = list(model.values())
            choice = random.choices(pages_list, weights=probabilities)
            model = transition_model(corpus, choice[0], damping_factor)
            for page in model:
                pagerank[page] += model[page]

    for page in pagerank:
        pagerank[page] = pagerank[page]/n

    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    model = {}
    for page in corpus:
        model[page] = 1/len(corpus)

    new_model = {}
    while abs(sum(new_model.values()) - sum(list(model.values()))) > 0.001:
        if new_model != {}:
            model = new_model
        for page in corpus:
            links_list = [x for x in corpus if page in corpus[x]]
            links_pagerank = 0
            for link in links_list:
                links_pagerank += model[link]/len(corpus[link])

            new_model[page] = ((1-damping_factor)/len(corpus)) + (damping_factor * links_pagerank)

    return new_model


if __name__ == "__main__":
    main()
